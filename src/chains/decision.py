from langchain.prompts import PromptTemplate
from llm.gemini import llm_init

decision_prompt = PromptTemplate.from_template("""
Given this structured query and clauses, make a decision.

Query:
{query}

Clauses:
{clauses}

Return JSON:
{{
  "decision": "approved" or "rejected",
  "amount": "$X" or null,
  "justification": "Explain with clause references"
}}
""")

def get_decision_chain():
    llm = llm_init()
    chain = decision_prompt | llm
    return chain