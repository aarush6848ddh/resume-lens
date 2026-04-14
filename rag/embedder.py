from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

def get_embeddings():
    return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")