import hashlib
import sys
from abc import ABC, abstractmethod
from dataclasses import asdict, dataclass, field
from datetime import datetime
from typing import Dict, List

from devchat.message import Message
from devchat.utils import get_logger, unix_to_local_datetime, user_id

logger = get_logger(__name__)


@dataclass
class Prompt(ABC):
    """
    A class to represent a prompt and its corresponding responses from the chat API.

    Attributes:
        model (str): The name of the language model.
        user_name (str): The name of the user.
        user_email (str): The email address of the user.
        _new_messages (dict): The messages for the current round of conversation.
        _history_messages (dict): The messages for the history of conversation.
        parent (str): The parent prompt hash.
        references (List[str]): The hashes of the referenced prompts.
        _timestamp (int): The timestamp when the response was created.
        _request_tokens (int): The number of tokens used in the request.
        _response_tokens (int): The number of tokens used in the response.
        _hash (str): The hash of the prompt.
    """

    model: str
    user_name: str
    user_email: str
    _new_messages: Dict = field(
        default_factory=lambda: {
            Message.INSTRUCT: [],
            "request": None,
            Message.CONTEXT: [],
            "responses": [],
        }
    )
    _history_messages: Dict[str, Message] = field(
        default_factory=lambda: {Message.CONTEXT: [], Message.CHAT: []}
    )
    parent: str = None
    references: List[str] = field(default_factory=list)
    _timestamp: int = 0
    _request_tokens: int = 0
    _response_tokens: int = 0
    _response_reasons: List[str] = field(default_factory=list)
    _hash: str = None

    def _complete_for_hashing(self) -> bool:
        """
        Check if the prompt is complete for hashing.

        Returns:
            bool: Whether the prompt is complete.
        """
        pass

    @property
    def new_context(self) -> List[Message]:
        pass

    @property
    def request(self) -> Message:
        pass

    @request.setter
    def request(self, value: Message):
        pass

    @property
    def responses(self) -> List[Message]:
        pass

    @property
    def timestamp(self) -> int:
        pass

    @timestamp.setter
    def timestamp(self, value: int):
        pass

    @property
    def request_tokens(self) -> int:
        pass

    @request_tokens.setter
    def request_tokens(self, value: int):
        pass

    @property
    def response_tokens(self) -> int:
        pass

    @response_tokens.setter
    def response_tokens(self, value: int):
        pass

    @abstractmethod
    def _count_response_tokens(self) -> int:
        """
        Calculate the number of tokens used in the responses.
        """

    @property
    def hash(self) -> str:
        pass

    @property
    @abstractmethod
    def messages(self) -> List[dict]:
        """
        List of messages in the prompt to be sent to the chat API.
        """

    @abstractmethod
    def input_messages(self, messages: List[dict]):
        """
        Input the messages from the chat API to new and history messages.
        The message list must follow the convention of the `messages` property.

        Args:
            messages (List[dict]): The messages from the chat API.
        """

    @abstractmethod
    def append_new(
        self, message_type: str, content: str, available_tokens: int = sys.maxsize
    ) -> bool:
        """
        Append a new message provided by the user to this prompt.

        Args:
            message_type (str): The type of the message.
            content (str): The content of the message.
            available_tokens (int): The number of tokens available for the message.

        Returns:
            bool: Whether the message is appended.
        """

    @abstractmethod
    def prepend_history(self, prompt: "Prompt", token_limit: int = sys.maxsize) -> bool:
        """
        Add the prompt to the beginning of the history messages.

        Args:
            prompt(Prompt): The prompt to prepend.
            token_limit (int): The max number of tokens for this prompt.

        Returns:
            bool: Whether the message is prepended.
        """

    @abstractmethod
    def set_request(self, content: str):
        """
        Set the request message for the prompt.

        Args:
            content (str): The request content to set.
        """

    @abstractmethod
    def set_response(self, response_str: str):
        """
        Parse the API response string and set the Prompt object's attributes.

        Args:
            response_str (str): The JSON-formatted response string from the chat API.
        """

    @abstractmethod
    def append_response(self, delta_str: str) -> str:
        """
        Append the content of a streaming response to the existing messages.

        Args:
            delta_str (str): The JSON-formatted delta string from the chat API.

        Returns:
            str: The delta content with index 0. None when the response is over.
        """

    def finalize_hash(self) -> str:
        """
        Calculate and set the hash of the prompt.

        Returns:
            str: The hash of the prompt. None if the prompt is incomplete.
        """
        pass

    def formatted_header(self) -> str:
        """Formatted string header of the prompt."""
        pass

    def formatted_footer(self, index: int) -> str:
        """Formatted string footer of the prompt."""
        pass

    def formatted_full_response(self, index: int) -> str:
        """
        Formatted full response of the prompt.

        Args:
            index (int): The index of the response to format.

        Returns:
            str: The formatted response string. None if the response is invalid.
        """
        pass

    def shortlog(self) -> List[dict]:
        """Generate a shortlog of the prompt."""
        pass
