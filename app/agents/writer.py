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
            - Organize the report with headings.
            - Use only the provided summaries.
            - Address important critique points whenever possible.
            - Do not invent facts.
            - Write in Markdown.
            """
        ),
        ("human", """
         Original Question:

        {question}

        Research Summaries:

        {summaries}

        Reviewer Feedback:

        {critiques}
         """
         )
    ]
)

writer_chain = writer_prompt | llm


def writer_node(state: ResearchState):

    question = state["question"]

    summaries = state["summaries"]

    critiques = state["critiques"]

    formatted_summaries = "\n\n".join(
        [
            f"Sub Question: {item['sub_question']}\n"
            f"Summary:\n{item['summary']}"
            for item in summaries
        ]
    )

    formatted_critiques = "\n".join(critiques)

    response = writer_chain.invoke(
        {
            "question": question,
            "summaries": formatted_summaries,
            "critiques": formatted_critiques,
        }
    )

    return {
        "final_report": response.content,
        "current_agent": "Writer",
        "agent_trace": [
            {
                "agent": "Writer",
                "action": "Generated final research report",
            }
        ],
    }