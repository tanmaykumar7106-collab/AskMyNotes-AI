from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain.embeddings import HuggingFaceEmbeddings

from langchain_chroma import Chroma


def create_vector_store(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="db"
    )

    return db