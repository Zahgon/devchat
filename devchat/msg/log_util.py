import json
import time
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

from devchat._cli.utils import get_model_config
from devchat.openai.openai_chat import OpenAIChat, OpenAIChatConfig, OpenAIPrompt
from devchat.store import Store
from devchat.workspace_util import USER_CHAT_DIR, get_workspace_chat_dir

from .user_info import user_info


@dataclass
class PromptData:
    model: str = "none"
    messages: Optional[List[Dict]] = field(default_factory=list)
    parent: Optional[str] = None
    references: Optional[List[str]] = field(default_factory=list)
    timestamp: int = time.time()
    request_tokens: int = 0
    response_tokens: int = 0


def gen_log_prompt(jsondata: Optional[str] = None, filepath: Optional[str] = None) -> OpenAIPrompt:
    """
    Generate a hash for a chat record
    """
    pass


def insert_log_prompt(prompt: OpenAIPrompt, workspace_path: Optional[str]) -> str:
    """
    Insert a chat record

    return the hash of the inserted chat record (prompt)
    """
    pass


def delete_log_prompt(hash: str, workspace_path: Optional[str]) -> Tuple[bool, Optional[str]]:
    """
    Delete a chat record

    return:
        success: True if the prompt is deleted successfully, False otherwise
    """
    pass
