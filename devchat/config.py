import os
import sys
from typing import Dict, List, Optional, Tuple

import oyaml as yaml
from pydantic import BaseModel


class GeneralProviderConfig(BaseModel):
    api_key: Optional[str]
    api_base: Optional[str]


class ModelConfig(BaseModel):
    max_input_tokens: Optional[int] = sys.maxsize
    provider: Optional[str]


class GeneralModelConfig(ModelConfig):
    max_tokens: Optional[int]
    stop_sequences: Optional[List[str]]
    temperature: Optional[float]
    top_p: Optional[float]
    top_k: Optional[int]
    stream: Optional[bool]


class ChatConfig(BaseModel):
    providers: Optional[Dict[str, GeneralProviderConfig]]
    models: Dict[str, GeneralModelConfig]
    default_model: Optional[str]


class ConfigManager:
    def __init__(self, dir_path: str):
        self.config_path = os.path.join(dir_path, "config.yml")
        if not os.path.exists(self.config_path):
            self._create_sample_file()
            self._file_is_new = True
        else:
            self._file_is_new = False
        self.config = self._load_and_validate_config()

    @property
    def file_is_new(self) -> bool:
        pass

    @property
    def file_last_modified(self) -> float:
        pass

    def _load_and_validate_config(self) -> ChatConfig:
        pass

    def model_config(self, model_id: Optional[str] = None) -> Tuple[str, ModelConfig]:
        pass

    def update_model_config(
        self, model_id: str, new_config: GeneralModelConfig
    ) -> GeneralModelConfig:
        pass

    def sync(self):
        pass

    def _create_sample_file(self):
        pass
