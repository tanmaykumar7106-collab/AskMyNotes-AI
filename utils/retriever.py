from utils.embeddings import create_embeddings
from utils.vectordb import search


def retrieve(query: str, top_k: int = 5):
    """
    Retrieve the most relevant chunks for a query.
    """

    query_embedding = create_embeddings([query])[0]

    results = search(query_embedding, top_k)

    return results