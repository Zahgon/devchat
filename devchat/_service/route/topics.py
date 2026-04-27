from typing import List, Optional

from fastapi import APIRouter, HTTPException, Query, status

from devchat._service.schema import request, response
from devchat.msg.topic_util import delete_topic as del_topic
from devchat.msg.topic_util import get_topic_shortlogs, get_topics

router = APIRouter()


@router.get("/{topic_root_hash}/logs", response_model=List[response.ShortLog])
def get_topic_logs(
    topic_root_hash: str,
    limit: int = Query(1, gt=0, description="maximum number of records to return"),
    offset: int = Query(0, ge=0, description="offset of the first record to return"),
    workspace: Optional[str] = Query(None, description="absolute path to the workspace/repository"),
):
    pass


@router.get("", response_model=List[response.TopicSummary])
def list_topics(
    limit: int = Query(1, gt=0, description="maximum number of records to return"),
    offset: int = Query(0, ge=0, description="offset of the first record to return"),
    workspace: Optional[str] = Query(None, description="absolute path to the workspace/repository"),
):
    pass


@router.post("/delete", response_model=response.DeleteTopic)
def delete_topic(
    item: request.DeleteTopic,
):
    pass
