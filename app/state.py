from typing import TypedDict, List, Optional, Annotated
import operator


class ResearchState(TypedDict):
    # User input
    question: str

    # Planner output
    sub_questions: List[str]

    # Researcher output
    search_results: List[dict]

    # Analyst output
    summaries: List[dict]

    # Critic output
    critiques: List[str]

    # Writer output
    final_report: str

    # Execution trace
    agent_trace: Annotated[List[dict], operator.add]

    # UI status
    current_agent: str

    # Final confidence
    confidence_score: Optional[float]