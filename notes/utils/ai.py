from django.conf import settings
from mistralai import Mistral

client=Mistral(api_key=settings.MISTRAL_API_KEY)

def summarize_text(text):
    try:
        response = client.chat.complete(
            model="mistral-small-latest",
            messages=[
                {"role": "system", "content": "Summarize the user's note in 3–4 bullet points."},
                {"role": "user", "content": text},
            ],
            max_tokens=200,
            temperature=0.4
        )

        return response.choices[0].message.content

    except Exception as er:
        return f"Mistral API Error: {er}"
