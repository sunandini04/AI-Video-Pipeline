import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_script(topic):
    prompt = f"Write an engaging YouTube video script about {topic}. Include an intro, main points, and conclusion."

    response = client.models.generate_content(
        model="models/gemini-2.5-flash",
        contents=prompt,
    )

    return response.text
