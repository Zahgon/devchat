import json
import os
import sys
from functools import wraps

from devchat.memory import ChatMemory

from .openai import (
    chat_completion_no_stream_return_json,
    chat_completion_stream,
    chat_completion_stream_commit,
    chunks_content,
    retry_timeout,
    stream_out_chunk,
    to_dict_content_and_call,
)
from .pipeline import exception_handle, pipeline, retry

chat_completion_stream_out = exception_handle(
    retry(
        pipeline(
            chat_completion_stream_commit,
            retry_timeout,
            stream_out_chunk,
            chunks_content,
            to_dict_content_and_call,
        ),
        times=3,
    ),
    lambda err: {
        "content": None,
        "function_name": None,
        "parameters": "",
        "error": err,
    },
)


def chat(
    prompt,
    memory: ChatMemory = None,
    stream_out: bool = False,
    model: str = os.environ.get("LLM_MODEL", "gpt-3.5-turbo-1106"),
    **llm_config,
):
    pass


def chat_json(
    prompt,
    memory: ChatMemory = None,
    model: str = os.environ.get("LLM_MODEL", "gpt-3.5-turbo-1106"),
    **llm_config,
):
    pass
