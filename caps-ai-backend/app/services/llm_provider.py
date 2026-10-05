import os
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional

try:
    from huggingface_hub import InferenceClient
except Exception:  # pragma: no cover
    InferenceClient = None  # type: ignore

try:
    from dotenv import load_dotenv
    from pathlib import Path
    _env_paths = [
        Path(__file__).resolve().parent.parent.parent / ".env",
        Path(__file__).resolve().parent.parent.parent.parent / ".env",
        Path(__file__).resolve().parent.parent.parent.parent / ".env.local",
    ]
    for _p in _env_paths:
        if _p.exists():
            load_dotenv(str(_p), override=False)
except Exception:
    pass


class BaseLLMProvider(ABC):
    """Provider-agnostic interface for text + tool-style LLM calls."""

    @abstractmethod
    def invoke(
        self,
        messages: List[Dict[str, str]],
        tools: Optional[List[Dict[str, Any]]] = None,
        temperature: float = 0.2,
        max_tokens: int = 1024,
    ) -> str:
        """Return a raw text response. Tool calling is handled by the caller."""


class HuggingFaceProvider(BaseLLMProvider):
    """Hugging Face Inference API provider. Works with any serverless endpoint,
    including Gemma family models hosted on the HF free tier.
    """

    def __init__(self, model: Optional[str] = None, api_key: Optional[str] = None):
        if InferenceClient is None:
            raise RuntimeError("huggingface_hub is not installed. Install it to use the HuggingFace provider.")
        self.model = model or os.getenv("HF_MODEL", "google/gemma-2-2b-it")
        self.api_key = api_key or os.getenv("HF_API_KEY")
        self.client = InferenceClient(
            provider="serverless",
            api_key=self.api_key,
        )

    def invoke(
        self,
        messages: List[Dict[str, str]],
        tools: Optional[List[Dict[str, Any]]] = None,
        temperature: float = 0.2,
        max_tokens: int = 1024,
    ) -> str:
        # Tool schemas are passed in the system prompt as structured text for
        # models that do not natively support tool calling. Native tool calling
        # can be enabled later when the model supports it.
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message.content or ""


class GoogleGeminiProvider(BaseLLMProvider):
    """Google Gemini provider with resilient multi-key, multi-model cascading failover.
    Automatically rotates keys on rate-limits (429/quota exhaustion) and cascades
    through the model pool before falling back to secondary providers.
    """

    DEFAULT_MODELS_POOL = [
        "models/gemini-flash-latest",
        "models/gemini-flash-lite-latest",
        "models/gemini-3.8-flash",
        "models/gemini-3.6-flash",
        "models/gemini-3.5-flash-lite",
        "models/gemini-3.1-flash-lite",
        "models/gemma-4-31b-it",
    ]

    def __init__(self, model: Optional[str] = None, api_key: Optional[str] = None, keys: Optional[List[str]] = None):
        # 1. Discover all Gemini keys from environment
        found_keys: List[str] = []
        if api_key:
            found_keys.append(api_key)
        for env_k, env_v in os.environ.items():
            if any(env_k.startswith(pfx) for pfx in ["GEMINI_API_KEY", "GEMINI_KEY", "GOOGLE_API_KEY"]):
                if env_v and env_v.strip() and env_v.strip() not in found_keys:
                    found_keys.append(env_v.strip())
        if keys:
            for k in keys:
                if k and k.strip() not in found_keys:
                    found_keys.append(k.strip())

        self.keys = found_keys
        self.active_key_idx = 0

        # 2. Build model pool
        self.models_pool = [model] if model else list(self.DEFAULT_MODELS_POOL)
        self.active_model_idx = 0

    @property
    def current_key(self) -> Optional[str]:
        if self.keys and self.active_key_idx < len(self.keys):
            return self.keys[self.active_key_idx]
        return None

    @property
    def current_model(self) -> str:
        if self.active_model_idx < len(self.models_pool):
            return self.models_pool[self.active_model_idx]
        return self.models_pool[0]

    def _rotate_target(self, reason: str = "Rate limit / quota exhausted"):
        """Rotate to next key, or advance to next model if all keys exhausted."""
        total_keys = max(1, len(self.keys))
        if self.active_key_idx + 1 < len(self.keys):
            self.active_key_idx += 1
            print(f"[LLM FAILOVER] Key rotated to [{self.active_key_idx + 1}/{total_keys}] for {self.current_model}: {reason}")
            return True
        elif self.active_model_idx + 1 < len(self.models_pool):
            self.active_key_idx = 0
            self.active_model_idx += 1
            print(f"[LLM FAILOVER] Advancing to next model [{self.active_model_idx + 1}/{len(self.models_pool)}]: {self.current_model}")
            return True
        return False

    def invoke(
        self,
        messages: List[Dict[str, str]],
        tools: Optional[List[Dict[str, Any]]] = None,
        temperature: float = 0.2,
        max_tokens: int = 1024,
    ) -> str:
        import json
        try:
            import requests
        except ImportError:
            requests = None

        max_attempts = min(15, max(1, len(self.keys)) * len(self.models_pool))
        attempts = 0

        # Format system instructions and conversation contents
        system_instructions = []
        contents = []
        for msg in messages:
            role = msg.get("role", "user")
            content = msg.get("content", "")
            if role == "system":
                system_instructions.append({"text": content})
            elif role == "assistant":
                contents.append({"role": "model", "parts": [{"text": content}]})
            else:
                contents.append({"role": "user", "parts": [{"text": content}]})

        body: Dict[str, Any] = {
            "contents": contents,
            "generationConfig": {
                "temperature": temperature,
                "maxOutputTokens": max_tokens,
            }
        }
        if system_instructions:
            body["systemInstruction"] = {"parts": system_instructions}

        while attempts < max_attempts:
            attempts += 1
            current_k = self.current_key
            current_m = self.current_model
            model_slug = current_m if current_m.startswith("models/") else f"models/{current_m}"
            url = f"https://generativelanguage.googleapis.com/v1beta/{model_slug}:generateContent?key={current_k}"

            try:
                if requests:
                    res = requests.post(url, json=body, timeout=12)
                    status_code = res.status_code
                    resp_data = res.json() if res.content else {}
                else:
                    import urllib.request
                    req = urllib.request.Request(
                        url,
                        data=json.dumps(body).encode("utf-8"),
                        headers={"Content-Type": "application/json"},
                        method="POST"
                    )
                    with urllib.request.urlopen(req, timeout=12) as response:
                        status_code = response.status
                        resp_data = json.loads(response.read().decode("utf-8"))

                if status_code == 200:
                    candidates = resp_data.get("candidates", [])
                    if candidates:
                        parts = candidates[0].get("content", {}).get("parts", [])
                        if parts:
                            return parts[0].get("text", "")
                    return ""

                # Non-200 status (e.g. 429 quota, 404 deprecated, 503 overloaded)
                err_msg = str(resp_data.get("error", {}).get("message", f"HTTP {status_code}"))
                print(f"[LLM WARNING] Gemini API returned {status_code} on {current_m}: {err_msg}")
                if self._rotate_target(reason=f"Status {status_code}: {err_msg}"):
                    continue
                break

            except Exception as e:
                print(f"[LLM WARNING] Gemini network/request error on {current_m}: {e}")
                if self._rotate_target(reason=str(e)):
                    continue
                break

        return ""


class ResilientFallbackProvider(BaseLLMProvider):
    """High-reliability composite provider:
    Attempts Google Gemini across all keys and models. If all are exhausted,
    falls back cleanly to Hugging Face serverless without crashing.
    """

    def __init__(self):
        self.gemini = GoogleGeminiProvider()
        self.hf = None
        if os.getenv("HF_API_KEY") and InferenceClient is not None:
            self.hf = HuggingFaceProvider()

    def invoke(
        self,
        messages: List[Dict[str, str]],
        tools: Optional[List[Dict[str, Any]]] = None,
        temperature: float = 0.2,
        max_tokens: int = 1024,
    ) -> str:
        # 1. Try Gemini multi-key / multi-model pool first
        if self.gemini.keys:
            res = self.gemini.invoke(messages, tools, temperature, max_tokens)
            if res:
                return res

        # 2. Fall back to Hugging Face if configured
        if self.hf:
            try:
                print("[LLM FAILOVER] Falling back to Hugging Face serverless provider...")
                return self.hf.invoke(messages, tools, temperature, max_tokens)
            except Exception as hf_err:
                print(f"[LLM WARNING] Hugging Face fallback failed: {hf_err}")

        # 3. Clean graceful degradation (never crashes callers)
        return ""


def get_llm_provider() -> BaseLLMProvider:
    """Returns resilient multi-key, multi-model provider with cascading failover."""
    return ResilientFallbackProvider()
