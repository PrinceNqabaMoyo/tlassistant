import os
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional

try:
    from huggingface_hub import InferenceClient
except Exception:  # pragma: no cover
    InferenceClient = None  # type: ignore


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
        "gemini-2.5-flash",
        "gemini-1.5-flash",
        "gemini-2.0-flash",
        "gemini-2.5-flash-lite",
        "gemini-1.5-pro",
    ]

    def __init__(self, model: Optional[str] = None, api_key: Optional[str] = None, keys: Optional[List[str]] = None):
        # 1. Discover all Gemini keys from environment
        found_keys: List[str] = []
        if api_key:
            found_keys.append(api_key)
        for env_var in ["GEMINI_API_KEY", "GOOGLE_API_KEY", "GEMINI_KEY_1", "GEMINI_KEY_2", "GEMINI_KEY_3"]:
            val = os.getenv(env_var)
            if val and val not in found_keys:
                found_keys.append(val)
        if keys:
            for k in keys:
                if k and k not in found_keys:
                    found_keys.append(k)

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
        max_attempts = min(10, max(1, len(self.keys)) * len(self.models_pool))
        attempts = 0

        while attempts < max_attempts:
            attempts += 1
            current_k = self.current_key
            current_m = self.current_model
            try:
                from langchain_google_genai import ChatGoogleGenerativeAI
                from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

                llm = ChatGoogleGenerativeAI(
                    model=current_m,
                    temperature=temperature,
                    convert_system_message_to_human=True,
                    google_api_key=current_k,
                )

                lc_messages = []
                for msg in messages:
                    role = msg.get("role", "user")
                    content = msg.get("content", "")
                    if role == "system":
                        lc_messages.append(SystemMessage(content=content))
                    elif role == "assistant":
                        lc_messages.append(AIMessage(content=content))
                    else:
                        lc_messages.append(HumanMessage(content=content))

                response = llm.invoke(lc_messages)
                return response.content if hasattr(response, "content") else str(response)

            except Exception as e:
                err_str = str(e).lower()
                is_quota = any(x in err_str for x in ["429", "quota", "resourceexhausted", "rate limit", "exhausted"])
                if is_quota and self._rotate_target(reason=str(e)):
                    continue  # Try next key or model
                print(f"[LLM WARNING] Gemini invoke error on {current_m}: {e}")
                if self._rotate_target(reason="General failure"):
                    continue
                break  # Circuit breaker: stop retrying

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
