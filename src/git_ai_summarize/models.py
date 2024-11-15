import os
from langchain_core.language_models.chat_models import BaseChatModel
from typing import List


def get_supported_providers() -> List[str]:
    """Get a list of supported providers."""
    return [
        "anthropic",
        "openai",
        "google",
        "mistral",
        "fireworks",
        "together",
        "vertex",
        "groq",
        "nvidia",
        "ollama",
        "ai21",
        "upstage",
        "databricks",
        "watsonx",
        "xai",
    ]


def get_model(provider_name: str | None, model_name: str | None) -> BaseChatModel:
    """Initialize and configure the LangChain components with specified model."""
    if provider_name == 'anthropic':
        from langchain_anthropic import ChatAnthropic
        model_class, api_key_env, api_url, api_key_param = ChatAnthropic, "ANTHROPIC_API_KEY", "https://www.anthropic.com", "anthropic_api_key"
    elif provider_name == 'openai':
        from langchain_openai import ChatOpenAI
        model_class, api_key_env, api_url, api_key_param = ChatOpenAI, "OPENAI_API_KEY", "https://platform.openai.com/account/api-keys", "openai_api_key"
    elif provider_name == 'google':
        from langchain_google_genai import ChatGoogleGenerativeAI
        model_class, api_key_env, api_url, api_key_param = ChatGoogleGenerativeAI, "GOOGLE_API_KEY", "https://developers.generativeai.google/", "google_api_key"
    elif provider_name == 'mistral':
        from langchain_mistralai import ChatMistralAI
        model_class, api_key_env, api_url, api_key_param = ChatMistralAI, "MISTRAL_API_KEY", "https://console.mistral.ai/api-keys/", "mistral_api_key"
    elif provider_name == 'fireworks':
        from langchain_fireworks import ChatFireworks
        model_class, api_key_env, api_url, api_key_param = ChatFireworks, "FIREWORKS_API_KEY", "https://app.fireworks.ai/", "fireworks_api_key"
    elif provider_name == 'together':
        from langchain_together import ChatTogether
        model_class, api_key_env, api_url, api_key_param = ChatTogether, "TOGETHER_API_KEY", "https://api.together.xyz/", "together_api_key"
    elif provider_name == 'vertex':
        from langchain_google_vertexai import ChatVertexAI
        model_class, api_key_env, api_url, api_key_param = ChatVertexAI, "GOOGLE_APPLICATION_CREDENTIALS", "https://cloud.google.com/vertex-ai", None
    elif provider_name == 'groq':
        from langchain_groq import ChatGroq
        model_class, api_key_env, api_url, api_key_param = ChatGroq, "GROQ_API_KEY", "https://console.groq.com/", "groq_api_key"
    elif provider_name == 'nvidia':
        from langchain_nvidia_ai_endpoints import ChatNVIDIA
        model_class, api_key_env, api_url, api_key_param = ChatNVIDIA, "NVIDIA_API_KEY", "https://api.nvidia.com/", "nvidia_api_key"
    elif provider_name == 'ollama':
        from langchain_ollama import ChatOllama
        model_class, api_key_env, api_url, api_key_param = ChatOllama, None, "https://ollama.ai/", None
    elif provider_name == 'ai21':
        from langchain_ai21 import ChatAI21
        model_class, api_key_env, api_url, api_key_param = ChatAI21, "AI21_API_KEY", "https://www.ai21.com/studio", "ai21_api_key"
    elif provider_name == 'upstage':
        from langchain_upstage import ChatUpstage
        model_class, api_key_env, api_url, api_key_param = ChatUpstage, "UPSTAGE_API_KEY", "https://upstage.ai/", "upstage_api_key"
    elif provider_name == 'databricks':
        from langchain_databricks import ChatDatabricks
        model_class, api_key_env, api_url, api_key_param = ChatDatabricks, "DATABRICKS_TOKEN", "https://www.databricks.com/", "databricks_token"
    elif provider_name == 'watsonx':
        from langchain_watsonx import ChatWatsonx
        model_class, api_key_env, api_url, api_key_param = ChatWatsonx, "WATSONX_API_KEY", "https://www.ibm.com/watsonx", "watsonx_api_key"
    elif provider_name == 'xai':
        from langchain_xai import ChatXAI
        model_class, api_key_env, api_url, api_key_param = ChatXAI, "XAI_API_KEY", "https://xai.com/", "xai_api_key"
    else:
        raise ValueError(f"Unsupported LLM provider: {provider_name}")

    max_tokens = 500

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
