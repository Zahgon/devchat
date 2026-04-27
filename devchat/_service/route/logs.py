from fastapi import APIRouter, HTTPException, status

from devchat._service.schema import request, response
from devchat.msg.log_util import delete_log_prompt, gen_log_prompt, insert_log_prompt

router = APIRouter()


@router.post("/insert", response_model=response.InsertLog)
def insert(
    item: request.InsertLog,
):
    pass


@router.post("/delete", response_model=response.DeleteLog)
def delete(
    item: request.DeleteLog,
):
    pass
