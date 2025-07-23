# model_loader.py
from langchain_openai import ChatOpenAI  # Make sure you install: pip install langchain-openai
from dotenv import load_dotenv
import os

load_dotenv()

def load_model():
    return ChatOpenAI(
        model="gpt-4o-mini",  # or "gpt-3.5-turbo"
        api_key= os.getenv("OPENAI_API_KEY"),  # ideally store in env variable
        temperature=0.0
    )
######################using this model_loader and working 