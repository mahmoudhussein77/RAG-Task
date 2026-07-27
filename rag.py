from vector_store import search
from llm import generate_answer


def ask_question(question):

    results = search(question, k=3)

    llm_response = generate_answer(question, results)

    found = llm_response.get("found", False)

    sources = []

    if found:

        for chunk in results:

            page = chunk["page"]

            if {"page": page} not in sources:
                sources.append(
                    {
                        "page": page
                    }
                )

    return {
        "answer": llm_response.get("answer", ""),
        "sources": sources,
        "found": found
    }