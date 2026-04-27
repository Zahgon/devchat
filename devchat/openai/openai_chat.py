import json
import os
from typing import Dict, Iterator, List, Optional, Union

from pydantic import BaseModel, Field

from devchat.chat import Chat
from devchat.utils import get_user_info, user_id

from .http_openai import stream_request
from .openai_message import OpenAIMessage
from .openai_prompt import OpenAIPrompt


class OpenAIChatParameters(BaseModel, extra="ignore"):
    temperature: Optional[float] = Field(0, ge=0, le=2)
    top_p: Optional[float] = Field(None, ge=0, le=1)
    n: Optional[int] = Field(None, ge=1)
    stream: Optional[bool] = Field(None)
    stop: Optional[Union[str, List[str]]] = Field(None)
    max_tokens: Optional[int] = Field(None, ge=1)
    presence_penalty: Optional[float] = Field(None, ge=-2.0, le=2.0)
    frequency_penalty: Optional[float] = Field(None, ge=-2.0, le=2.0)
    logit_bias: Optional[Dict[int, float]] = Field(None)
    user: Optional[str] = Field(None)
    request_timeout: Optional[int] = Field(32, ge=3)


class OpenAIChatConfig(OpenAIChatParameters):
    """
    Configuration object for the OpenAIChat APIs.
    """

    model: str


class OpenAIChat(Chat):
    """
    OpenAIChat class that handles communication with the OpenAI Chat API.
    """

    def __init__(self, config: OpenAIChatConfig):
        """
        Initialize the OpenAIChat class with a configuration object.

        Args:
            config (OpenAIChatConfig): Configuration object with parameters for the OpenAI Chat API.
        """
        self.config = config

    def init_prompt(self, request: str, function_name: Optional[str] = None) -> OpenAIPrompt:
        pass

    def load_prompt(self, data: dict) -> OpenAIPrompt:
        pass

    def complete_response(self, prompt: OpenAIPrompt) -> str:
        pass

    def stream_response(self, prompt: OpenAIPrompt) -> Iterator:
        pass
