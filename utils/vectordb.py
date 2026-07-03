import chromadb
import uuid
from pathlib import Path

# Create database directory if it doesn't exist
DB_PATH = Path("db")
DB_PATH.mkdir(exist_ok=True)

# Initialize ChromaDB client
client = chromadb.PersistentClient(path=str(DB_PATH))

# Create / Load collection
collection = client.get_or_create_collection(
    name="ask_my_notes"
)


def add_documents(chunks, embeddings, metadata):
    """
    Store document chunks into ChromaDB.
    """

    ids = [str(uuid.uuid4()) for _ in chunks]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist(),
        metadatas=metadata
    )


def search(query_embedding, top_k=5):
    """
    Search the vector database.
    """

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=top_k
    )

    return results


def clear_database():
    """
    Delete all stored documents.
    """

    global collection

    client.delete_collection("ask_my_notes")

    collection = client.get_or_create_collection(
        name="ask_my_notes"
    )


def total_documents():
    return collection.count()