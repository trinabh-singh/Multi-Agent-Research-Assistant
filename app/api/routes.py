from fastapi import APIRouter
import time

from app.graph.workflow import graph

from app.api.schemas import (
    ResearchRequest,
    ResearchResponse,
)

router = APIRouter()


@router.post(
    "/research",
    response_model=ResearchResponse,
)
def research(request: ResearchRequest):

    initial_state = {
        "question": request.question,
        "sub_questions": [],
        "search_results": [],
        "summaries": [],
        "critiques": [],
        "final_report": "",
        "agent_trace": [],
        "current_agent": "",
        "confidence_score": None,
    }

    start = time.perf_counter()

    result = graph.invoke(initial_state)

    execution_time = round(
        time.perf_counter() - start,
        2,
    )

    return ResearchResponse(
        report=result["final_report"],
        trace=result["agent_trace"],
        execution_time=execution_time,
    )