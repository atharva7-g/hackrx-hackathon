from utils.defs import PROJECT_ROOT, CHUNK_OVERLAP, CHUNK_SIZE
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os


def load_documents(path):
    loader = PyPDFLoader(path)
    docs = loader.load()
    return docs

def split_documents(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    return splitter.split_documents(docs)

