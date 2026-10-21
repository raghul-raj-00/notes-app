from django.conf import settings
from groq import Groq

client = Groq(api_key=settings.GROQ_API_KEY)


def summarize_text(text):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "Summarize the user's note in  2-3 lines."},
                {"role": "user", "content": text},
            ],
            max_tokens=200,
            temperature=0.4
        )

        return response.choices[0].message.content

    except Exception as er:
        return f"Groq API Error: {er}"

def generate_answer(question, context):
    try:
        prompt = f"""Answer only from the provided context.
        Context:
        {context}
        Question:
        {question}
        """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content
    except Exception as er:
        return f"Groq API Error: {er}"
