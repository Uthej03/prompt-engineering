import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

def get_completion(prompt, model="gemini-3.5-flash-lite"):
    response = client.models.generate_content(
        model=model,
        contents=prompt
    )

    return response.text