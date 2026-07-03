import os
import streamlit as st

from utils.pdf_loader import load_pdf

st.set_page_config(
    page_title="Ask My Notes",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Ask My Notes")

uploaded_file = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)

if uploaded_file:

    os.makedirs("temp", exist_ok=True)

    pdf_path = os.path.join(
        "temp",
        uploaded_file.name
    )

    with open(pdf_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    documents = load_pdf(pdf_path)

    st.success(
        f"Successfully loaded {len(documents)} pages."
    )

    with st.expander("Preview Pages"):

        for i, doc in enumerate(documents):

            st.markdown(f"### Page {i+1}")

            st.write(doc.page_content[:500])

            st.divider()