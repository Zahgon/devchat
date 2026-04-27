from pathlib import Path
from typing import List

import oyaml as yaml
from fastapi import APIRouter
from fastapi.responses import JSONResponse

from devchat._service.schema import response
from devchat.utils import get_logger, rmtree
from devchat.workflow.namespace import (
    WorkflowMeta,
    get_prioritized_namespace_path,
    iter_namespace,
)
from devchat.workflow.path import (
    CHAT_CONFIG_FILENAME,
    CHAT_DIR,
    CUSTOM_BASE,
    CUSTOM_CONFIG_FILE,
    WORKFLOWS_BASE,
    WORKFLOWS_CONFIG_FILENAME,
)
from devchat.workflow.update_util import (
    HAS_GIT,
    copy_workflows_usr,
    custom_update_by_git,
    update_by_git,
    update_by_zip,
)

router = APIRouter()

logger = get_logger(__name__)


@router.get("/list", response_model=List[WorkflowMeta])
def list_workflow():
    pass


@router.get("/config")
def get_config():
    pass


@router.post("/update", response_model=response.UpdateWorkflows)
def update_workflows():
    pass


@router.post("/custom_update", response_model=response.UpdateWorkflows)
def update_custom_workflows():
    pass
