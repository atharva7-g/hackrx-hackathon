from langchain_google_genai import ChatGoogleGenerativeAI
from utils.defs import config_init

def llm_init():
    config_init()

    return ChatGoogleGenerativeAI(
        model="gemini-2.5-pro",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )

