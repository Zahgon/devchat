import os
from typing import Dict, List, Optional

from devchat._cli.utils import get_model_config
from devchat.openai.openai_chat import OpenAIChat, OpenAIChatConfig
from devchat.store import Store
from devchat.workspace_util import USER_CHAT_DIR, get_workspace_chat_dir


def get_topic_shortlogs(
    topic_root_hash: str, limit: int, offset: int, workspace_path: Optional[str]
) -> List[Dict]:
    pass


def get_topics(
    limit: int, offset: int, workspace_path: Optional[str], with_deleted: bool = False
) -> List[Dict]:
    pass


def delete_topic(topic_hash: str, workspace_path: Optional[str]):
    """
    Logicalily delete a topic
    """
    pass
