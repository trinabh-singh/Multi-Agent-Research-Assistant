from graph.workflow import graph

initial_state = {
    "question": "How is AI changing healthcare?",
    "sub_questions": [],
    "search_results": [],
    "summaries": [],
    "critiques": [],
    "final_report": "",
    "agent_trace": [],
    "current_agent": "",
    "confidence_score": None,
}

for event in graph.stream(
    initial_state,
    stream_mode="updates",
):

    print(event)