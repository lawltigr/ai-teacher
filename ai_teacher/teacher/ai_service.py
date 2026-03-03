from openai import OpenAI
from django.conf import settings

client = OpenAI(api_key=settings.OPENAI_API_KEY)

def generate_answer(style, user_message):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": style.prompt_template},
            {"role": "user", "content": user_message}
        ]
    )
    return response.choices[0].message.content