from app.state import (
    ResearchState,
    ResearchResult,
)

from app.tools.web_search import search_web


def researcher_node(state: ResearchState):

    sub_questions = state["sub_questions"]

    search_results: list[ResearchResult] = []

    for question in sub_questions:

        results = search_web(question)

        search_results.append(
            {
                "sub_question": question,
                "results": results,
            }
        )

    return {
        "search_results": search_results,
        "current_agent": "Researcher",
        "agent_trace": [
            {
                "agent": "Researcher",
                "status": "completed",
                "message": f"Searched {len(sub_questions)} topics",
            }
        ],
    }