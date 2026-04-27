from datetime import datetime
from enum import Enum
from typing import Any, Tuple

from devchat.utils import unix_to_local_datetime, user_id
from devchat.workflow.workflow import Workflow

from .user_info import user_info


class MessageType(Enum):
    """
    Enum for message types
    """

    CHATTING = "chatting"  # chat with LLM directly
    WORKFLOW = "workflow"  # trigger a workflow


def mk_meta() -> Tuple[str, str]:
    """
    Make metadata for a response
    """
    pass


def route_message_by_content(message_content: str) -> Tuple[MessageType, Any]:
    """
    Route the message to the correct handler
    1. trigger a workflow
    2. chat with LLM directly
    """
    pass
