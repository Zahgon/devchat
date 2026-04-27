import os
from functools import wraps

import requests

BASE_SERVER_URL = os.environ.get("DEVCHAT_IDE_SERVICE_URL", "http://localhost:3000")


def rpc_call(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        pass

    return wrapper


def rpc_method(f):
    """
    Decorator for Service methods
    """

    @wraps(f)
    def wrapper(self, *args, **kwargs):
        pass

    return wrapper
