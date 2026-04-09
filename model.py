from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI



def get_model():
    load_dotenv() # Load environment variables from .env file
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)
    return model
