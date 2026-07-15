from langchain_core.prompts import ChatPromptTemplate

from app.config import llm
from app.state import ResearchState


writer_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are an expert technical research writer.

            Using the provided summaries and reviewer feedback,
            write a professional research report.

            Requirements:

            - Answer the original question.
            - Organize with Markdown headings.
            - Use only the supplied summaries.
            - Address reviewer feedback whenever possible.
            - Do not invent facts.
            """
                    ),
                    (
                        "human",
                        """
            Original Question:

            {question}

            Research Summaries:

            {summaries}

            Reviewer Feedback:

            {critiques}
            """
        ),
    ]
)

writer_chain = writer_prompt | llm


def writer_node(state: ResearchState):

    formatted_summaries = "\n\n".join(
        [
            f"Sub Question: {item['sub_question']}\n"
            f"Summary:\n{item['summary']}"
            for item in state["summaries"]
        ]
    )

    formatted_critiques = "\n\n".join(state["critiques"])

    try:

        response = writer_chain.invoke(
            {
                "question": state["question"],
                "summaries": formatted_summaries,
                "critiques": formatted_critiques,
            }
        )
    except Exception as e:
        raise RuntimeError(f"Writer Agent Failed: {e}")

    return {
        "final_report": response.content,
        "current_agent": "Writer",
        "agent_trace": [
            {
                "agent": "Writer",
                "status": "completed",
                "message": "Generated final markdown report",
            }
        ],
    }