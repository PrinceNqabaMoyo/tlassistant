---
name: production-security-fundamentals
description: Production hardening, security, socket lifecycle, and reliability runbook. Enforces connection pooling, CPU sandboxing, query bounds, circuit breakers, and POPIA child privacy compliance.
---

# Production Hardening, Security & Reliability Runbook

This skill embodies core software engineering and systems design fundamentals (as emphasized by Andrew Ng's AI Engineering Skills Map, Austin's C# post-mortems, and Abhishek Singh's backend reliability manifesto).
Use this runbook when authoring backend routes, integrating external APIs, handling database queries, or reviewing code for production readiness.

---

## 1. Socket Lifecycle & Connection Pooling (Austin Incident #1 Prevention)

### The Anti-Pattern: Socket Exhaustion in Request Handlers
```python
# ❌ DANGEROUS ANTI-PATTERN: Creates a new client per request.
# Under concurrent load, sockets remain in TIME_WAIT, exhausting OS file descriptors.
@router.post("/api/tutor/ask")
async def ask_tutor(payload: TutorRequest):
    async with httpx.AsyncClient() as client:
        res = await client.post("https://api.groq.com/...", ...)
```

### The Production Standard: Lifespan Singleton Client with Pool Limits
Always maintain a single persistent client across the application lifecycle:
```python
# ✅ PRODUCTION PATTERN: Reused pooled client with connection limits
class LLMClientPool:
    _client: httpx.AsyncClient | None = None

    @classmethod
    def get_client(cls) -> httpx.AsyncClient:
        if cls._client is None or cls._client.is_closed:
            limits = httpx.Limits(max_keepalive_connections=20, max_connections=100)
            timeout = httpx.Timeout(10.0, connect=3.0)
            cls._client = httpx.AsyncClient(limits=limits, timeout=timeout)
        return cls._client

    @classmethod
    async def close(cls):
        if cls._client and not cls._client.is_closed:
            await cls._client.aclose()
```

---

## 2. Memory Projections & Query Bounding (Austin Incident #2 Prevention)

### The Anti-Pattern: Unbounded Database Reads
```python
# ❌ DANGEROUS ANTI-PATTERN: Pulls all documents and all fields into Python RAM.
# With 10,000 learners, this triggers multi-gigabyte memory spikes and OOM container kills.
sessions = db.collection("session_index").where("userId", "==", user_id).get()
```

### The Production Standard: Projections, Indexes & Pre-Aggregated Snapshots
1. **Field Masking (Projection):** Fetch only the fields needed:
   ```python
   query = db.collection("session_index").where("userId", "==", user_id).select(["score", "timestamp", "topic"]).limit(20)
   ```
2. **Pre-Aggregated Mastery Snapshots:**
   Never scan historical sessions to recompute mastery on every page load. Maintain a single `mastery_snapshot` document updated incrementally upon session completion, reducing Firestore reads by 97.5%.
3. **Cursor Pagination:** Always paginate using `order_by()` and `start_after()` for table feeds.

---

## 3. CPU Sandboxing & Event Loop Non-Blocking (FastAPI Concurrency)

### The Anti-Pattern: CPU-Bound Computation in Async Endpoints
SymPy calculations (e.g. polynomial factoring, equation solving, canonical graph building) are CPU-bound. If called directly in an `async def` FastAPI route, they block the single-threaded asyncio event loop, causing all concurrent requests to stall:
```python
# ❌ DANGEROUS ANTI-PATTERN: Blocks the entire ASGI event loop
@router.post("/api/math/solve")
async def solve_expression(payload: ExprPayload):
    result = sympy.factor(payload.expr) # Event loop is frozen here
    return {"result": str(result)}
```

### The Production Standard: Thread Sandboxing with Hard Timeouts
```python
# ✅ PRODUCTION PATTERN: Offloads CPU work to threadpool with strict timeout
import asyncio

@router.post("/api/math/solve")
async def solve_expression(payload: ExprPayload):
    try:
        # Offload to worker thread with a 2.5s maximum execution budget
        result = await asyncio.wait_for(
            asyncio.to_thread(sympy.factor, payload.expr),
            timeout=2.5
        )
        return {"result": str(result)}
    except asyncio.TimeoutError:
        logger.warning(f"SymPy evaluation timed out for expression: {payload.expr}")
        raise HTTPException(status_code=408, detail="Computation complexity limit exceeded.")
```

---

## 4. Blast Radius Control & Graceful Degradation (Abhishek Backend Manifesto)

Fundile operates on a zero-panic design principle: **External dependencies (LLMs, payment gateways, network CDNs) WILL fail. The core student learning loop must NEVER break.**

1. **Circuit Breaker to Deterministic Hints:**
   If the Gemini or Groq API times out or rate limits:
   ```python
   try:
       response = await call_llm_tutor(context)
   except Exception as err:
       logger.error(f"LLM Provider failure: {err}. Falling back to deterministic Tier 2 hint.")
       # Return deterministic pre-baked rule hint; student never sees an error modal
       return {"type": "hint_tier2", "content": prebaked_tier2_hint, "fallback": True}
   ```
2. **Express Homework Lane:**
   Homework submissions bypass batch evaluation queues, writing to local telemetry buffers and returning immediate feedback.

---

## 5. Shift-Left Security & POPIA Child Privacy (Section 35)

Because Fundile serves South African high school students (minors):
1. **Zero Device GPS Polling:** Under POPIA Sec 35, tracking minors' geographic coordinates is strictly illegal. Regionalization must occur solely through voluntary dropdowns (Province / School) and coarse edge IP headers.
2. **PII Egress Sanitization:** User names, email addresses, and school IDs must be stripped before sending prompts to external LLMs. Prompts receive only anonymous, topic-bound diagnostic context.
3. **No Unsanitized HTML (`innerHTML`):** All mathematical, tabular, and textual inputs must be parsed with `DOMParser` or React safe elements. `dangerouslySetInnerHTML` is strictly prohibited.
4. **Secrets Discipline:** Never allow hardcoded fallback secrets (e.g. `SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret'`). In production, missing secrets must trigger immediate fast-fail.
