import streamlit as st
from pathlib import Path

from config import APP_NAME

# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(
    page_title="AskMyNotes AI",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# Session State
# ==========================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "documents" not in st.session_state:
    st.session_state.documents = []

if "db_ready" not in st.session_state:
    st.session_state.db_ready = False

# ==========================================
# Sidebar
# ==========================================

with st.sidebar:

    st.title("📚 AskMyNotes AI")

    st.divider()

    uploaded_files = st.file_uploader(
        "Upload PDF(s)",
        type=["pdf"],
        accept_multiple_files=True
    )

    st.divider()

    st.subheader("📄 Uploaded Documents")

    if len(st.session_state.documents) == 0:
        st.info("No documents uploaded.")

    else:
        for doc in st.session_state.documents:
            st.success(doc)

    st.divider()

    st.subheader("⚙ Settings")

    model = st.selectbox(
        "Ollama Model",
        [
            "llama3",
            "mistral",
            "gemma3"
        ]
    )

# ==========================================
# Main Page
# ==========================================

st.title(APP_NAME)

st.caption("Offline RAG powered by Ollama + ChromaDB")

st.divider()

# Chat Messages

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input

question = st.chat_input("Ask anything about your documents...")