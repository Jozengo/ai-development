from autogen_ext.models.openai import OpenAIChatCompletionClient

from backends.app.core.config import settings


def _setup_model_client():
    """设置模型客户端"""
    model_config = {
        "model": settings.LLM_MODEL,
        "api_key": settings.OPENAI_API_KEY,
        "model_info": {
            "vision": False,
            "function_calling": True,
            "json_output": True,
            "family": "unknown",
        },
    }

    if settings.OPENAI_API_BASE:
        model_config["base_url"] = settings.OPENAI_API_BASE

    return OpenAIChatCompletionClient(**model_config)

model_client = _setup_model_client()