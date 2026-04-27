import json
import sys
from dataclasses import dataclass
from typing import List, Optional

from devchat.message import Message
from devchat.prompt import Prompt
from devchat.utils import get_logger, openai_message_tokens, openai_response_tokens, update_dict

from .openai_message import OpenAIMessage

logger = get_logger(__name__)


@dataclass
class OpenAIPrompt(Prompt):
    """
    A class to represent a prompt and its corresponding responses from OpenAI APIs.
    """

    _id: str = None

    @property
    def id(self) -> str:
        pass

    @property
    def messages(self) -> List[dict]:
        pass

    def input_messages(self, messages: List[dict]):
        pass

    def append_new(
        self, message_type: str, content: str, available_tokens: int = sys.maxsize
    ) -> bool:
        pass

    def set_functions(self, functions, available_tokens: int = sys.maxsize):
        pass

    def get_functions(self):
        pass

    def _prepend_history(
        self, message_type: str, message: Message, token_limit: int = sys.maxsize
    ) -> bool:
        pass

    def prepend_history(self, prompt: "OpenAIPrompt", token_limit: int = sys.maxsize) -> bool:
        # Prepend the first response and the request of the prompt
        pass

    def set_request(self, content: str, function_name: Optional[str] = None) -> int:
        pass

    def set_response(self, response_str: str):
        """
        Parse the API response string and set the Prompt object's attributes.

        Args:
            response_str (str): The JSON-formatted response string from the chat API.
        """
        pass

    def append_response(self, delta_str: str) -> str:
        """
        Append the content of a streaming response to the existing messages.

        Args:
            delta_str (str): The JSON-formatted delta string from the chat API.

        Returns:
            str: The delta content with index 0. None when the response is over.
        """
        pass

    def _count_response_tokens(self) -> int:
        pass

    def _validate_model(self, response_data: dict):
        pass

    def _timestamp_from_dict(self, response_data: dict):
        pass

    def _id_from_dict(self, response_data: dict):
        pass
