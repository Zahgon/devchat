"""
openai api call by PYTHON http client
"""

import http.client
import json
import os
import ssl
import sys
from urllib.parse import urlparse


class LineReader:
    """read line from stream"""

    def __init__(self, response):
        self.response = response

    def __iter__(self):
        return self

    def __next__(self):
        line = self.response.readline()
        if not line:
            raise StopIteration
        line = line.strip()
        if not line:
            return self.__next__()
        line = line.decode("utf-8")
        if not line.startswith("data:"):
            print("Receive invalid line: {line}", end="\n\n", file=sys.stderr)
            raise ValueError(f"Invalid line: {line}")

        if line[5:].strip() == "[DONE]":
            raise StopIteration
        try:
            return json.loads(line[5:])
        except json.JSONDecodeError as err:
            print(f"Error decoding JSON: {err}", end="\n\n", file=sys.stderr)
            raise ValueError(f"Invalid line: {line}") from err


def stream_response(connection: http.client.HTTPSConnection, data, headers):
    """stream response from openai api"""
    pass


def stream_request(api_key, api_base, data):
    """stream request to openai api"""
    pass
