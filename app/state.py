from typing import TypedDict, List, Optional, Annotated
import operator


class SearchResult(TypedDict):
    title: str
    url: str
    content: str
    score: float


class ResearchResult(TypedDict):
    sub_question: str
    results: List[SearchResult]


class Summary(TypedDict):
    sub_question: str
    summary: str


class ResearchState(TypedDict):
    # User input
    question: str

    # Planner output
    sub_questions: List[str]

    # Researcher output
    search_results: List[ResearchResult]

    # Analyst output
    summaries: List[Summary]

    # Critic output
    critiques: List[str]

    # Writer output
    final_report: str

    # Execution trace
    agent_trace: Annotated[List[dict], operator.add]

    # UI status
    current_agent: str

    # Confidence score
    confidence_score: Optional[float]