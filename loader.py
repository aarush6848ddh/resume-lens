from langchain_community.document_loaders import PyPDFLoader

def load_pdf(file_path):
    output = ""
    loader = PyPDFLoader(file_path)
    for page in loader.load_and_split():
        output += page.page_content
    return output 

if __name__ == "__main__":
    text = load_pdf("FALL.pdf")
    print(text[:500]) # Print the first 500 characters of the loaded PDF text