import getpass
import os
import socket
import subprocess
from typing import Optional, Tuple


class UserInfo:
    def __init__(self):
        self._name = None
        self._email = None

        self._load_user_info()

    @property
    def name(self) -> str:
        pass

    @property
    def email(self) -> str:
        pass

    def _load_user_info(self):
        """
        Load user info
        """
        pass

    def __get_git_user_info(self) -> Tuple[Optional[str], Optional[str]]:
        """
        Load user info from git
        """
        pass

    def __get_sys_user_name(self) -> str:
        """
        Get user name from system
        """
        pass


user_info = UserInfo()
