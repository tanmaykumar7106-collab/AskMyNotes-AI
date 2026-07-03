import ollama


SYSTEM_PROMPT = """
You are an AI assistant that answers questions ONLY using the provided context.

If the answer is not present in the context, say:

'I couldn't find that information in the uploaded documents.'

Do not make up information.
"""


def ask_llm(context, question, model="llama3"):

    prompt = f"""
Context:
{context}

Question:
{question}

Answer:
"""

    response = ollama.chat(
        model=model,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]