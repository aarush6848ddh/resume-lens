from langchain.schema import Document   
from loader import load_pdf                                                                              
from rag.splitter import split_documents                                                                 
from rag.embedder import get_embeddings                                                                  
from rag.vector_store import build_vectorstore, get_retriever                                            
from rag.rag_chain import build_rag_chain

def build_resume_rag(resume_path, extra_docs=None):
    text = load_pdf(resume_path)
    all_docs = [Document(page_content=text, metadata={"source": "resume"})]
    if extra_docs:
        all_docs += extra_docs
    chunks = split_documents(all_docs)
    embeddings = get_embeddings()
    vector_store = build_vectorstore(chunks, embeddings)
    retriever = get_retriever(vector_store, k=3)
    return build_rag_chain(retriever)



    
    
