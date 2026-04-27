import os
import shutil
import tempfile
import zipfile
from datetime import datetime
from pathlib import Path
from typing import List, Optional, Tuple

import requests

from devchat.utils import get_logger, rmtree
from devchat.workflow.path import (
    CHAT_DIR,
    CUSTOM_BASE,
    WORKFLOWS_BASE_NAME,
)

HAS_GIT = False
try:
    from git import GitCommandError, InvalidGitRepositoryError, Repo
except ImportError:
    pass
else:
    HAS_GIT = True


REPO_NAME = "workflows"
DEFAULT_BRANCH = "scripts"
REPO_URLS = [
    # url, branch
    ("https://gitlab.com/devchat-ai/workflows.git", DEFAULT_BRANCH),
    ("git@github.com:devchat-ai/workflows.git", DEFAULT_BRANCH),
    ("https://github.com/devchat-ai/workflows.git", DEFAULT_BRANCH),
]
ZIP_URLS = [
    "https://gitlab.com/devchat-ai/workflows/-/archive/scripts/workflows-scripts.zip",
    "https://codeload.github.com/devchat-ai/workflows/zip/refs/heads/scripts",
]

# TODO: logger setting
logger = get_logger(__name__)


def _backup(workflow_base: Path, n: int = 5) -> Optional[Path]:
    """
    Backup the current workflow base dir to zip with timestamp under .backup.

    Args:
        n: the number of backups to keep, default 3

    Returns:
        Path: the backup zip path
    """
    pass


def _download_zip_to_dir(candidate_urls: List[str], dst_dir: Path) -> bool:
    """
    Download the zip file with the first successful url
    in the candidate_urls to the target_dir.

    Args:
        candidate_urls: the list of candidate urls
        dst_dir: the dst dir of the extracted zip file, should not exist

    Returns:
        bool: True if success else False
    """
    pass


def _clone_repo_to_dir(candidates: List[Tuple[str, str]], dst_dir: Path) -> bool:
    """
    Clone the git repo with the first successful url
    in the candidates to the dst_dir.

    Args:
        candidates: the list of candidate git url and branch pairs.
        dst_dir: the dst dir of the cloned repo, should not exist

    Returns:
        bool: True if success else False
    """
    pass


def update_by_zip(workflow_base: Path) -> Tuple[bool, str]:
    pass


def update_by_git(workflow_base: Path) -> Tuple[bool, str]:
    pass


def custom_update_by_git(workflow_base: Path, repo_urls=REPO_URLS) -> Tuple[bool, str]:
    pass


def copy_workflows_usr():
    """
    Copy workflows/usr to scripts/custom/usr for engine migration.
    """
    pass
