from pydantic import BaseModel
from typing import Dict, List, Optional, Tuple, Union
from pydantic import ValidationError, validator
import logging

logger = logging.getLogger(__name__)


class GeneratePayload_InValue(BaseModel):
    in_value: Dict[str, Union[int, float, str, bool, Dict, List]]


class GeneratePayload_OutType(BaseModel):
    out_type: Dict[str, str]


class GeneratePayload(BaseModel, smart_union=True):
    prompt: str
    out_type: Dict[str, str]
    model_name: str
    prompt_template: Optional[str] = None
    max_tokens: Optional[int] = None
