import json
import sys
import time
from typing import Iterator, List, Optional

from devchat.chat import Chat
from devchat.message import Message
from devchat.openai.openai_prompt import OpenAIPrompt
from devchat.store import Store
from devchat.utils import get_logger

logger = get_logger(__name__)


class Assistant:
    def __init__(self, chat: Chat, store: Store, max_prompt_tokens: int, need_store: bool):
        """
        Initializes an Assistant object.

        Args:
            chat (Chat): A Chat object used to communicate with chat APIs.
        """
        self._chat = chat
        self._store = store
        self._prompt = None
        self.token_limit = max_prompt_tokens
        self._need_store = need_store

    @property
    def prompt(self) -> OpenAIPrompt:
        pass

    @property
    def available_tokens(self) -> int:
        pass

    def _check_limit(self):
        pass

    def make_prompt(
        self,
        request: str,
        instruct_contents: Optional[List[str]],
        context_contents: Optional[List[str]],
        functions: Optional[List[dict]],
        parent: Optional[str] = None,
        references: Optional[List[str]] = None,
        function_name: Optional[str] = None,
    ):
        """
        Make a prompt for the chat API.

        Args:
            request (str): The user request.
            instruct_contents (Optional[List[str]]): A list of instructions to the prompt.
            context_contents (Optional[List[str]]): A list of context messages to the prompt.
            parent (Optional[str]): The parent prompt hash. None means a new topic.
            references (Optional[List[str]]): The reference prompt hashes.
        """
        pass

    def iterate_response(self) -> Iterator[str]:
        """Get an iterator of response strings from the chat API.

        Returns:
            Iterator[str]: An iterator over response strings from the chat API.
        """
        pass
