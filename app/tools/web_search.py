from dotenv import load_dotenv
import os

from tavily import TavilyClient

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


def search_web(query: str):
    try:
        response = client.search(
            query=query,
            search_depth="advanced",
            max_results=3,
        )
    
    except Exception as e:
        raise RuntimeError(f"Tavily Search Failed: {e}")

    cleaned_results = []

    for result in response.get("results", []):

        cleaned_results.append(
            {
                "title": result["title"],
                "url": result["url"],
                "content": result["content"],
                "score": result["score"],
            }
        )

    return cleaned_results