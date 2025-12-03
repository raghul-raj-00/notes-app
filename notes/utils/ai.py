import requests
from django.conf import settings

def summarize_text(text):
    url = "https://api.deepseek.com/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {settings.DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": "Summarize the user's note into 3–4 clear bullet points."},
            {"role": "user", "content": text}
        ],
        "max_tokens": 150,
        "temperature": 0.4
    }

    response = requests.post(url, json=data, headers=headers)
    response_data = response.json()

    try:
        return response_data["choices"][0]["message"]["content"]
    except:
        return "Error: Could not generate summary."
