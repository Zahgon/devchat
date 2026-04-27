import os
import re
from typing import List, Optional


class Namespace:
    def __init__(self, root_path: str, branches: List[str] = None):
        """
        :param root_path: The root path of the namespace.
        :param branches: The hidden branches with ascending order of priority.
        """
        self.root_path = root_path
        self.branches = branches if branches else ["sys", "org", "usr"]

    @staticmethod
    def is_valid_name(name: str) -> bool:
        """
        Check if a name is valid.

        A valid name is either an empty string or
        a sequence of one or more alphanumeric characters, hyphens, or underscores,
        separated by single dots. Each component cannot contain a dot.

        :param name: The name to check.
        :return: True if the name is valid, False otherwise.
        """
        pass

    def get_file(self, name: str, file: str) -> Optional[str]:
        """
        :param name: The command name in the namespace.
        :param file: The target file name.
        :return: The full path of the target file in the command directory.
        """
        pass

    def list_files(self, name: str) -> List[str]:
        """
        :param name: The command name in the namespace.
        :return: The full paths of the files in the command directory.
        """
        pass

    def list_names(self, name: str = "", recursive: bool = False) -> List[str]:
        """
        :param name: The command name in the namespace. Defaults to the root.
        :param recursive: Whether to list all descendant names or only child names.
        :return: A list of all names under the given name.
        """
        pass

    def _add_dirnames_to_commands(self, full_path: str, name: str, commands: set):
        pass

    def _add_recursive_dirnames_to_commands(self, full_path: str, name: str, commands: set):
        pass

    def _recursive_dir_walk(self, full_path: str, name: str, commands: set):
        pass
