import os
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_mistralai import ChatMistralAI
from langchain_fireworks import ChatFireworks
from langchain_together import ChatTogether
from langchain_google_vertexai import ChatVertexAI
from langchain_groq import ChatGroq
from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain_ollama import ChatOllama
from langchain_ai21 import ChatAI21
from langchain_upstage import ChatUpstage
from langchain_databricks import ChatDatabricks
from langchain_ibm import ChatWatsonx
from langchain_xai import ChatXAI
from typing import List


def get_supported_providers() -> List[str]:
    """Get a list of supported providers."""
    return [
        "anthropic",
        "openai",
        "google",
        "mistralai",
        "fireworks",
        "together",
        "vertexai",
        "groq",
        "nvidia_ai",
        "ollama",
        "ai21",
        "upstage",
        "databricks",
        "watsonx",
        "xai",
    ]


def get_model(provider_name: str | None, model_name: str | None) -> BaseChatModel:
    """Initialize and configure the LangChain components with specified model."""
    providers = {
        "anthropic": (ChatAnthropic, "ANTHROPIC_API_KEY", "https://www.anthropic.com", "anthropic_api_key"),
        "openai": (ChatOpenAI, "OPENAI_API_KEY", "https://platform.openai.com/account/api-keys", "openai_api_key"),
        "google": (ChatGoogleGenerativeAI, "GOOGLE_API_KEY", "https://developers.generativeai.google/", "google_api_key"),
        "mistral": (ChatMistralAI, "MISTRAL_API_KEY", "https://console.mistral.ai/api-keys/", "mistral_api_key"),
        "fireworks": (ChatFireworks, "FIREWORKS_API_KEY", "https://app.fireworks.ai/", "fireworks_api_key"),
        "together": (ChatTogether, "TOGETHER_API_KEY", "https://api.together.xyz/", "together_api_key"),
        "vertex": (ChatVertexAI, "GOOGLE_APPLICATION_CREDENTIALS", "https://cloud.google.com/vertex-ai", None),
        "groq": (ChatGroq, "GROQ_API_KEY", "https://console.groq.com/", "groq_api_key"),
        "nvidia": (ChatNVIDIA, "NVIDIA_API_KEY", "https://api.nvidia.com/", "nvidia_api_key"),
        "ollama": (ChatOllama, None, "https://ollama.ai/", None),
        "ai21": (ChatAI21, "AI21_API_KEY", "https://www.ai21.com/studio", "ai21_api_key"),
        "upstage": (ChatUpstage, "UPSTAGE_API_KEY", "https://upstage.ai/", "upstage_api_key"),
        "databricks": (ChatDatabricks, "DATABRICKS_TOKEN", "https://www.databricks.com/", "databricks_token"),
        "watsonx": (ChatWatsonx, "WATSONX_API_KEY", "https://www.ibm.com/watsonx", "watsonx_api_key"),
        "xai": (ChatXAI, "XAI_API_KEY", "https://xai.com/", "xai_api_key"),
    }

    max_tokens = 500

    if provider_name not in providers:
        raise ValueError(f"Unsupported LLM provider: {provider_name}")

    model_class, api_key_env, api_url, api_key_param = providers[provider_name]

    if api_key_env:
        api_key = os.getenv(api_key_env)
        if not api_key:
            raise ValueError(
                f"{api_key_env} environment variable not set. "
                f"Get an API key from {api_url}"
            )

        kwargs = {
            "model": model_name,
            "max_tokens": max_tokens,
            "streaming": True
        }

        if api_key_param:
            kwargs[api_key_param] = api_key

        return model_class(**kwargs)

    return model_class(
        model=model_name,
        max_tokens=500,
        streaming=True
    )
