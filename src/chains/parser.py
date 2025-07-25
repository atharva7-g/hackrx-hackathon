from langchain_google_genai import ChatGoogleGenerativeAI
from llm.gemini import llm_init
from langchain_core.prompts import ChatPromptTemplate

def get_query_parser_chain():
    llm = llm_init()

    prompt = ChatPromptTemplate.from_messages([
        ("system",
         "You are an expert assistant that parses natural language insurance queries to extract structured information."),
        ("human",
         "Given a query like: '46-year-old male, knee surgery in Pune, 3-month-old insurance policy', extract the following details as structured JSON:\n\n- age (integer)\n- gender (male/female/other)\n- procedure (string)\n- location (string)\n- policy_duration_months (integer)\n\nRespond ONLY with a JSON object, no extra explanation."),
        ("human", "Query: {query}")
    ])

    chain = prompt | llm
    return chain

