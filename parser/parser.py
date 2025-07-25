from langchain_google_genai import ChatGoogleGenerativeAI
from config import config_init

EXAMPLE_QUERY = "46-year-old male, knee surgery in Pune, 3-month-old insurance policy"
DOCUMENTS_PATH = "./data/documents"

config_init()

def create_gemini_llm():
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-pro",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
    )

messages = [
    ("system", "You are an expert assistant that parses natural language insurance queries to extract structured information."),

    ("human", "Given a query like: '46-year-old male, knee surgery in Pune, 3-month-old insurance policy', extract the following details as structured JSON:\n\n- age (integer)\n- gender (male/female/other)\n- procedure (string)\n- location (string)\n- policy_duration_months (integer)\n\nRespond ONLY with a JSON object, no extra explanation."),

    ("human", f"Query: {EXAMPLE_QUERY}")
]

llm = create_gemini_llm()

response = llm.invoke(messages)

print(response.content)