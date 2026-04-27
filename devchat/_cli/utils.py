import os
import sys
import zipfile
from contextlib import contextmanager
from typing import Any, List, Optional, Tuple

from devchat._cli.errors import MissContentInPromptException
from devchat.utils import add_gitignore, find_root_dir, get_logger, rmtree, setup_logger

logger = get_logger(__name__)


def download_and_extract_workflow(workflow_url, target_dir):
    pass


@contextmanager
def handle_errors():
    # import openai
    """Handle errors in the CLI."""
    pass


REPO_CHAT_DIR = None
USER_CHAT_DIR = None


def init_dir() -> Tuple[str, str]:
    """
    Initialize the chat directories.

    Returns:
        REPO_CHAT_DIR: The chat directory in the repository.
        USER_CHAT_DIR: The chat directory in the user's home.
    """
    pass


def valid_git_repo(target_dir: str, valid_urls: List[str]) -> bool:
    """
    Check if a directory is a valid Git repository and if its URL is in a list of valid URLs.

    :param target_dir: The path of the directory to check.
    :param valid_urls: A list of valid Git repository URLs.
    :return: True if the directory is a valid Git repository with a valid URL, False otherwise.
    """
    pass


def clone_git_repo(target_dir: str, repo_urls: List[Tuple[str, str]]):
    """
    Clone a Git repository from a list of possible URLs.

    :param target_dir: The path where the repository should be cloned.
    :param repo_urls: A list of possible Git repository URLs.
    """
    pass


def get_model_config(user_chat_dir: str, model: Optional[str] = None) -> Tuple[str, Any]:
    pass
