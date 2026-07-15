from app.graph.workflow import graph

initial_state = {
    "question": "How is Generative AI changing healthcare?",
    "sub_questions": [],
    "search_results": [],
    "summaries": [],
    "critiques": [],
    "final_report": "",
    "agent_trace": [],
    "current_agent": "",
    "confidence_score": None,
}

result = graph.invoke(initial_state)

print(result["final_report"])