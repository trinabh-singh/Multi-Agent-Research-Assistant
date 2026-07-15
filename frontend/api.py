import requests

API_URL = "http://127.0.0.1:8000/research"


def generate_report(question: str):

    response = requests.post(
        API_URL,
        json={
            "question": question
        },
        timeout=300,
    )

    response.raise_for_status()

    return response.json()