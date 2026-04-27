import json
from typing import Iterator, List, Optional

from devchat._cli.utils import get_model_config
from devchat.assistant import Assistant
from devchat.openai.openai_chat import OpenAIChat, OpenAIChatConfig
from devchat.path import USER_CHAT_DIR
from devchat.store import Store
from devchat.utils import parse_files
from devchat.workspace_util import get_workspace_chat_dir


def _get_model_and_config(model: Optional[str], config_str: Optional[str]):
    pass


def chatting(
    content: str,
    model_name: str,
    parent: Optional[str],
    workspace: Optional[str],
    context_files: Optional[List[str]],
) -> Iterator[str]:
    pass
