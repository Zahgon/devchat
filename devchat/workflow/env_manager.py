import hashlib
import os
import shutil
import subprocess
import sys
from typing import Dict, Optional, Tuple

import virtualenv

from devchat.utils import get_logger, get_logging_file

from .envs import MAMBA_BIN_PATH
from .path import CHAT_CONFIG_FILENAME, CHAT_DIR, ENV_CACHE_DIR, MAMBA_PY_ENVS, MAMBA_ROOT
from .schema import ExternalPyConf
from .user_setting import USER_SETTINGS

PYPI_TUNA = "https://pypi.tuna.tsinghua.edu.cn/simple"
DEFAULT_CONDA_FORGE_URL = "https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/"


logger = get_logger(__name__)


def _get_external_envs() -> Dict[str, ExternalPyConf]:
    """
    Get the external python environments info from the user settings.
    """
    external_pythons: Dict[str, ExternalPyConf] = {}
    for conf in USER_SETTINGS.external_workflow_python:
        external_pythons[conf.env_name] = conf

    return external_pythons


EXTERNAL_ENVS = _get_external_envs()


class PyEnvManager:
    mamba_bin = MAMBA_BIN_PATH
    mamba_root = MAMBA_ROOT

    def __init__(self):
        pass

    @staticmethod
    def get_py_version(py: str) -> Optional[str]:
        """
        Get the version of the python executable.
        """
        pass

    @staticmethod
    def get_dep_hash(reqirements_file: str) -> str:
        """
        Get the hash of the requirements file content.

        Used to check if the requirements file has been changed.
        """
        pass

    def ensure(
        self,
        env_name: str,
        py_version: Optional[str] = None,
        reqirements_file: Optional[str] = None,
    ) -> Optional[str]:
        """
        Ensure the python environment exists with the given name and version.
        And install the requirements if provided.

        return the python executable path.
        """
        pass

    def create_with_virtualenv(self, env_name: str) -> Tuple[bool, str]:
        """
        Create a new python environment using virtualenv with the current Python interpreter.
        """
        pass

    def install(self, env_name: str, requirements_file: str) -> Tuple[bool, str]:
        """
        Install or update requirements in the python environment.

        Args:
            env_name: the name of the python environment
            requirements_file: the absolute path to the requirements file.

        Returns:
            A tuple (success, message), where success is a boolean indicating
            whether the installation was successful, and message is a string
            containing output or error information.
        """
        pass

    def should_reinstall(self, env_name: str, requirements_file: str) -> bool:
        """
        Check if the requirements file has been changed.
        """
        pass

    def create(self, env_name: str, py_version: str) -> Tuple[bool, str]:
        """
        Create a new python environment using mamba.
        """
        pass

    def remove(self, env_name: str, py_version: Optional[str] = None) -> bool:
        pass

    def remove_by_del(self, env_name: str) -> bool:
        """
        Remove the python environment.
        """
        pass

    def remove_by_mamba(self, env_name: str) -> bool:
        """
        Remove the python environment.
        """
        pass

    def get_py(self, env_name: str) -> Optional[str]:
        """
        Get the python executable path of the given environment.
        """
        pass

    def _get_conda_forge_url(self) -> str:
        """
        Read the conda-forge URL from the config file.
        If the config file does not exist or does not contain the conda-forge URL,
        use the default value.
        """
        pass
