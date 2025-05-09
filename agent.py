# agent.py

import os
import google.generativeai as genai
from dotenv import load_dotenv
from tools import available_tools  # optional if you use tools inside agent logic

# Load .env file
load_dotenv()

# Get API key from environment
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("models/gemini-1.5-flash")

def run_agent(user_input: str) -> str:
    try:
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"
