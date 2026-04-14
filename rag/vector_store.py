from langchain_chroma import Chroma 

def build_vectorstore(chunks, embeddings):
    vector_store = Chroma.from_documents(documents=chunks, embedding=embeddings)
    return vector_store

def get_retriever(vectorstore, k=3):
    return vectorstore.as_retriever(search_kwargs={"k": k})