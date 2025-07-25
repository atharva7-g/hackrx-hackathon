from src.retrieval.loader import load_documents
from src.retrieval.loader import split_documents
from src.retrieval.vectorstores import create_vectorstore
from src.chains.parser import get_query_parser_chain
from src.chains.decision import get_decision_chain
from utils.defs import PROJECT_ROOT
import os

BASE_DIR = os.path.dirname(PROJECT_ROOT)
DOC_DIR = os.path.join(BASE_DIR, "data", "documents")



if __name__ == "__main__":
    docs = load_documents(os.path.join(DOC_DIR, "doc1.pdf"))
    chunks = split_documents(docs)

    vs = create_vectorstore(chunks)
    retriever = vs.as_retriever()

    query_input = "46-year-old male, knee surgery in Pune, 3-month-old insurance policy"
    parser_chain = get_query_parser_chain()
    structured_query = parser_chain.invoke({"query": query_input})

    if not isinstance(structured_query.content, str):
        raise ValueError(f"Expected string for embedding, got {type(structured_query.content)}")

    relevant_docs = retriever.invoke(structured_query.content)

    clause_text = "\n\n".join([doc.page_content for doc in relevant_docs])

    decision_chain = get_decision_chain()
    decision = decision_chain.invoke({"query": structured_query, "clauses": clause_text})

    print(decision.content)

