from autogen_core.models import ModelFamily
from autogen_ext.models.openai import OpenAIChatCompletionClient


def _setup_model_config():
    model_config = {
        "model": "deepseek-chat",
        "base_url": "https://api.deepseek.com/v1",
        "api_key": "sk-650c182cb76c4c429e6b27e1f59b9189",
        "model_info": {
            "vision": False,
            "function_calling": True,
            "json_output": True,
            "structured_output": True,
            "family": ModelFamily.UNKNOWN
        }
    }
    return OpenAIChatCompletionClient(**model_config)


model_client = _setup_model_config()
