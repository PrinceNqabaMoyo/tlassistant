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
    """Google Gemini provider. Kept for easy fallback while testing HF."""

    def __init__(self, model: Optional[str] = None, api_key: Optional[str] = None):
        self.model = model or os.getenv("GEMINI_MODEL", "models/gemini-1.5-flash")
        self.api_key = api_key or os.getenv("GOOGLE_API_KEY")
        self._llm = None

    def _get_llm(self):
        if self._llm is None:
            from langchain_google_genai import ChatGoogleGenerativeAI
            self._llm = ChatGoogleGenerativeAI(
                model=self.model,
                temperature=0.2,
                convert_system_message_to_human=True,
                google_api_key=self.api_key,
            )
        return self._llm

    def invoke(
        self,
        messages: List[Dict[str, str]],
        tools: Optional[List[Dict[str, Any]]] = None,
        temperature: float = 0.2,
        max_tokens: int = 1024,
    ) -> str:
        llm = self._get_llm()
        # Convert simple message dicts to LangChain message types
        from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
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


def get_llm_provider() -> BaseLLMProvider:
    """Returns the configured provider based on environment variables.

    Priority:
      1. HF_API_KEY set -> HuggingFace provider (HF_MODEL defaults to gemma-2-2b-it)
      2. GOOGLE_API_KEY set -> Gemini provider
    """
    if os.getenv("HF_API_KEY"):
        return HuggingFaceProvider()
    return GoogleGeminiProvider()
