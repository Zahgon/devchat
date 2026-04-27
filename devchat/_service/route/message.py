import os
from typing import Iterator, Optional

from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from devchat._service.schema import request, response
from devchat.msg.chatting import chatting
from devchat.msg.util import MessageType, mk_meta, route_message_by_content
from devchat.workflow.workflow import Workflow

router = APIRouter()


@router.post("/msg")
def msg(
    message: request.UserMessage,
):
    pass
