import os
import re

from .namespace import Namespace


class RecursivePrompter:
    def __init__(self, namespace: Namespace):
        self.namespace = namespace

    def run(self, name: str) -> str:
        pass

    def _replace_file_references(self, prompt_file_path: str, content: str) -> str:
        # prompt_file_path is the path to the file that contains the content
        # @relative file path@: file is relative to the prompt_file_path
        pass
