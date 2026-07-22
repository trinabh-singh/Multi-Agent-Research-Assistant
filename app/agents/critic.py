from langchain_core.prompts import ChatPromptTemplate

from config import llm
from state import ResearchState


critic_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are an expert research critic.

            Evaluate the factual accuracy and completeness
            of the provided summaries.

            Identify:

            - Missing information
            - Unsupported claims
            - Contradictions
            - Weak evidence

            Return concise bullet points.
            """
        ),
        (
            "human",
            """
            Research Summaries:

            {summaries}
            """
        ),
    ]
)

critic_chain = critic_prompt | llm


def critic_node(state: ResearchState):

    summaries = state["summaries"]

    formatted_summaries = "\n\n".join(
        [
            f"Sub Question: {item['sub_question']}\n"
            f"Summary:\n{item['summary']}"
            for item in summaries
        ]
    )
    try:

        response = critic_chain.invoke(
            {
                "summaries": formatted_summaries,
            }
        )
    except Exception as e:
        raise RuntimeError(f"Critic Agent Failed: {e}")
    return {
        "critiques": [response.content],
        "current_agent": "Critic",
        "agent_trace": [
            {
                "agent": "Critic",
                "status": "completed",
                "message": "Reviewed report quality",
            }
        ],
    }