from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from util.keys.api_key import get_openai_apikey

def load_vector_store(vector_store_path:str):
    embeddings = OpenAIEmbeddings(api_key=get_openai_apikey())

    new_vector_store = FAISS.load_local(
        vector_store_path, embeddings, allow_dangerous_deserialization=True
    )

    return new_vector_store
