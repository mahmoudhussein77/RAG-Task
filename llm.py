from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_answer(query, retrieved_chunks):
    context = "\n\n".join(
        chunk["text"] for chunk in retrieved_chunks
    )

    prompt = f"""
You are an AI assistant for Question Answering over documents.

You MUST answer ONLY using the provided context.

If the answer is explicitly present in the context:
Return ONLY this JSON:

{{
    "answer": "...",
    "found": true
}}

If the answer is NOT present in the context:
Return ONLY this JSON:

{{
    "answer": "I couldn't find the answer in the provided document.",
    "found": false
}}

Rules:
- Use ONLY the provided context.
- Never use your own knowledge.
- Never guess.
- If the context is insufficient, do not infer missing information.
- Keep the answer concise.
- Return ONLY valid JSON.
- Do NOT wrap the JSON inside markdown.
- Do NOT add any explanation.
- Note that the contex file which you answer based on it is called "NexaFlow S200"

Context:
{context}

Question:
{query}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0,
            response_format={"type": "json_object"}
        )

        text = response.choices[0].message.content.strip()

        if text.startswith("```"):
            text = text.replace("```json", "")
            text = text.replace("```", "")
            text = text.strip()

        result = json.loads(text)

        if "answer" not in result:
            result["answer"] = ""

        if "found" not in result:
            result["found"] = False

        return result

    except Exception as e:
        print(f"LLM Error: {e}")

        return {
            "answer": "I couldn't find the answer in the provided document.",
            "found": False
        }