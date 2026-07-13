from dotenv import load_dotenv
import os

from tavily import TavilyClient

load_dotenv()

client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)

def search_web(query: str):

    results = client.search(
        query=query,
        search_depth="advanced",
        max_results=3
    )

    return results.get("results", [])