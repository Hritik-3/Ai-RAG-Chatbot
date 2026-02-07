from openai import OpenAI
from app.config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def ask_llm(question, context):
    prompt = f"""Answer ONLY using the context below.
Context:
{context}

Question:
{question}
"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


# We force OpenAI to answer using context only.