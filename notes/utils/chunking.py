from langchain_text_splitters import RecursiveCharacterTextSplitter
def chunk_text(text):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    return text_splitter.split_text(text)