from pydantic import BaseModel
from typing import List, Dict, Any


class ResearchRequest(BaseModel):
    question: str


class ResearchResponse(BaseModel):
    report: str
    execution_time: float
    trace: List[Dict[str, Any]]