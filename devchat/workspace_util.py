import os
from typing import Optional

from .path import USER_CHAT_DIR


def _ensure_workspace_chat_dir(workspace_path: str) -> str:
    """
    Ensure the workspace chat directory exists and is ignored by git

    return the chat directory path
    """
    pass


def get_workspace_chat_dir(workspace_path: Optional[str]) -> str:
    """
    Get the chat directory for a workspace
    Return user chat directory if workspace is None
    """
    pass
