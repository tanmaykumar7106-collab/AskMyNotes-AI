from sentence_transformers import SentenceTransformer

# Load model only once
_model = None

def get_embedding_model():
    global _model

    if _model is None:
        print("🔄 Loading embedding model...")
        _model = SentenceTransformer("all-MiniLM-L6-v2")
        print("✅ Embedding model loaded.")

    return _model


def create_embeddings(text_chunks):
    """
    Convert list of text chunks into embeddings.
    """

    model = get_embedding_model()

    embeddings = model.encode(
        text_chunks,
        convert_to_numpy=True,
        show_progress_bar=True,
        normalize_embeddings=True
    )

    return embeddings