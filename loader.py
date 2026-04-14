from langchain_community.document_loaders import PyPDFLoader

def load_pdf(file_path):
    with open(file_path, "r") as f:
        return f.read()

if __name__ == "__main__":
    text = load_pdf("FALL.txt")
    print(text[:500]) # Print the first 500 characters of the loaded PDF text