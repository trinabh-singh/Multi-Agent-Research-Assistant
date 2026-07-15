from langgraph.graph import StateGraph, END

from app.state import ResearchState

from app.agents.planner import planner_node
from app.agents.researcher import researcher_node
from app.agents.analyst import analyst_node
from app.agents.critic import critic_node
from app.agents.writer import writer_node

workflow = StateGraph(ResearchState)

workflow.add_node(
    "planner",
    planner_node
)
workflow.add_node(
    "researcher",
    researcher_node,
)

workflow.add_node(
    "analyst",
    analyst_node,
)

workflow.add_node(
    "critic",
    critic_node,
)

workflow.add_node(
    "writer",
    writer_node,
)

workflow.set_entry_point(
    "planner"
)

workflow.add_edge(
    "planner",
    "researcher",
)

workflow.add_edge(
    "researcher",
    "analyst",
)

workflow.add_edge(
    "analyst",
    "critic",
)

workflow.add_edge(
    "critic",
    "writer",
)

workflow.add_edge(
    "writer",
    END,
)

graph = workflow.compile()