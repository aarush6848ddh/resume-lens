from langchain_core.runnables import RunnablePassthrough                                                 
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate                                                    
from model import get_model

model = get_model()

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs) 

def build_rag_chain(retriever):
     prompt = ChatPromptTemplate.from_template("Use the following context to answer the question.\nContext: {context}\nQuestion: {question}")
     return ({"context": retriever | format_docs, "question": RunnablePassthrough()} | prompt | model | StrOutputParser())
