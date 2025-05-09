# AI Task Agent with Gemini & Streamlit

This project is an intelligent, conversational AI agent built with [Google's Gemini API](https://ai.google.dev/) and a simple [Streamlit](https://streamlit.io/) interface. Users can ask questions or issue commands, and the agent responds using Google's powerful generative models.

## Features

- Conversational AI with Gemini 1.5 Flash
- Task-oriented agent behavior
- Lightweight Streamlit frontend
- Secure API key handling with `.env`
- Extensible: plug in additional tools or logic


# Setup Instructions:
1) Clone the repo:


python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

2) Create Virtual Environment:

git clone https://github.com/your-username/ai-task-agent.git
cd ai-task-agent


3) Install depedencies:

pip install -r requirements.txt

4) Set your .env file:

Create a .env file and add your Gemini API key:
GOOGLE_API_KEY=your_gemini_api_key_here


5) Run the app:


streamlit run app.py


