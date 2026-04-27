import logging
import os
import sys

from gunicorn.app.base import BaseApplication
from gunicorn.glogging import Logger
from loguru import logger

from devchat._service.config import config
from devchat.workspace_util import get_workspace_chat_dir


class InterceptHandler(logging.Handler):
    def emit(self, record):
        # get corresponding Loguru level if it exists
        pass


class StubbedGunicornLogger(Logger):
    def setup(self, cfg):
        pass


class StandaloneApplication(BaseApplication):
    """Our Gunicorn application."""

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super().__init__()

    def load_config(self):
        pass

    def load(self):
        pass


def run_with_gunicorn(app):
    pass


# https://pawamoy.github.io/posts/unify-logging-for-a-gunicorn-uvicorn-app/
