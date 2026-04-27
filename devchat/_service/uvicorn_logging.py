import logging
import os
import sys

from loguru import logger

from devchat._service.config import config
from devchat.workspace_util import get_workspace_chat_dir


class InterceptHandler(logging.Handler):
    def emit(self, record):
        # get corresponding Loguru level if it exists
        pass


def setup_logging():
    # intercept everything at the root logger
    pass
