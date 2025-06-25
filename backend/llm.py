import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Modern client (this is the correct usage for openai>=1.x)
client = OpenAI()

SYSTEM_PROMPT = (
    "You are a helpful assistant. Use only the provided context to answer questions. "
    "If the answer is not present, say 'I couldn't find that in the document.'"
)

def build_prompt(context_chunks, question):
    context = "\n\n".join(context_chunks)
    return f"""Use the following context to answer the question.

Context:
{context}

Question: {question}
"""

def get_answer_from_openai(chunks, query):
    query_prompt = build_prompt(chunks, query)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": query_prompt}
        ],
        temperature=0.2,
    )

    return response.choices[0].message.content.strip()
