from dotenv import load_dotenv
import os

load_dotenv()  

api_key = os.getenv("PEXELS_API_KEY")
print("Your Pexels API Key is:", api_key)
