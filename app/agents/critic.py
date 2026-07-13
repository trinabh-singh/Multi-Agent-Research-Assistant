from langchain_core.prompts import ChatPromptTemplate
from app.config import llm
from app.state import ResearchState


critic_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are an expert research critic.

            Evaluate the factual accuracy and completeness of the provided summaries.

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

    response = critic_chain.invoke(
        {
            "summaries": formatted_summaries
        }
    )

    critiques = [response.content]

    return {
        "critiques": critiques,
        "current_agent": "Critic",
        "agent_trace": [
            {
                "agent": "Critic",
                "action": f"Evaluated {len(summaries)} summaries",
            }
        ],
    }