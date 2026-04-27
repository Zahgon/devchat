import ast
import json
from dataclasses import asdict, dataclass, field, fields
from typing import Dict, Optional

from devchat.message import Message


@dataclass
class OpenAIMessage(Message):
    role: str = None
    name: Optional[str] = None
    function_call: Dict[str, str] = field(default_factory=dict)

    def __post_init__(self):
        if not self._validate_role():
            raise ValueError("Invalid role. Must be one of 'system', 'user', or 'assistant'.")

        if not self._validate_name():
            raise ValueError(
                "Invalid name. Must contain a-z, A-Z, 0-9, and underscores, "
                "with a maximum length of 64 characters."
            )

    def to_dict(self) -> dict:
        pass

    @classmethod
    def from_dict(cls, message_data: dict) -> "OpenAIMessage":
        pass

    def function_call_to_json(self):
        '''
        convert function_call to json
        function_call is like this:
        {
            "name": function_name,
            "arguments": '{"key": """value"""}'
        }
        '''
        pass

    def stream_from_dict(self, message_data: dict) -> str:
        """Append to the message from a dictionary returned from a streaming chat API."""
        pass

    def _validate_role(self) -> bool:
        """Validate the role attribute.

        Returns:
            bool: True if the role is valid, False otherwise.
        """
        pass

    def _validate_name(self) -> bool:
        """Validate the name attribute.

        Returns:
            bool: True if the name is valid or None, False otherwise.
        """
        pass

    def _validate_string(self, string: str) -> bool:
        """Validate a string attribute.

        Returns:
            bool: True if the string is valid or None, False otherwise.
        """
        pass
