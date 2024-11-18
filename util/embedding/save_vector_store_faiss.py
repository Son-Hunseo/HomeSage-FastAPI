from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from util.keys.api_key import get_openai_apikey

def save_vector_store(file_path:str, vector_store_path:str):
    loader = CSVLoader(file_path=file_path, encoding="utf-8")
    data = loader.load()

    embeddings = OpenAIEmbeddings(api_key=get_openai_apikey())

    vector_store = FAISS.from_documents(data, embeddings)
    vector_store.save_local(vector_store_path)