from langchain_core.prompts import ChatPromptTemplate
from app.config import llm
from app.state import ResearchState

analyst_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are an expert research analyst.

            Given one research sub-question and its web search results,
            write a factual summary.

            Rules:

            - Use only the provided evidence.
            - Do not invent facts.
            - Keep it under 150 words.
            - Mention disagreements if sources conflict.
            """
        ),
        ("human",
        """
        Sub Question:

        {sub_question}

        Search Results:

        {results}
        """
        )
    ]
)

analyst_chain = analyst_prompt | llm

def analyst_node(state: ResearchState):

    search_results = state["search_results"]

    summaries = []

    for item in search_results:
        
        response = analyst_chain.invoke(
            {
                "sub_question": item["sub_question"],
                "results": item["results"]
            }
        )
        summaries.append(
        {
            "sub_question": item["sub_question"],
            "summary": response.content
        }
    )
    

    return {
        "summaries": summaries,
        "current_agent": "Analyst",
        "agent_trace": [
            {
                "agent": "Analyst",
                "action": f"Analyzed search results for {len(search_results)} sub-questions"
            }
        ]
    }