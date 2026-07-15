from langchain_core.prompts import ChatPromptTemplate
from app.config import llm
from app.state import ResearchState


planner_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are an expert research planner.

            Break every research question into
            3-5 focused research sub-questions.

            Return only the questions.
            """
        ),
        ("human", "{question}")
    ]
)

planner_chain = planner_prompt | llm


def planner_node(state: ResearchState):

    question = state["question"]
    try:
        response = planner_chain.invoke(
            {
                "question": question
            }
        )
    
    except Exception as e:
        raise RuntimeError(f"Planner Agent Failed: {e}")

    sub_questions = [
        line.strip("-123456789. ")
        for line in response.content.split("\n")
        if line.strip()
    ] 

    return {
        "sub_questions": sub_questions,
        "current_agent": "Planner",
        "agent_trace": [
            {
                "agent": "Planner",
                "status": "completed",
                "message": f"Generated {len(sub_questions)} sub-questions",
            }
        ]
    }