import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
import streamlit as st
from dotenv import load_dotenv
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI

# Load environment variables from .env file
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Check if API key is set
if not api_key:
    st.error("❌ OPENAI_API_KEY is not set. Please check your .env file.")
    st.stop()

# Streamlit UI layout
st.set_page_config(page_title="Ask a Question from your PDF")
st.title("📄 Ask a Question from your PDF")

# Upload the PDF
uploaded_file = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_file is not None:
    # Save the file temporarily
    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Load and split the PDF
    loader = UnstructuredPDFLoader(uploaded_file.name)
    docs = loader.load()

    # Text splitter
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(docs)

    # Preview extracted content
    with st.expander("📑 Extracted PDF Text Preview"):
        for i, chunk in enumerate(texts[:3]):
            st.write(f"Chunk {i + 1}:", chunk.page_content)
        st.write("📦 Total Chunks:", len(texts))

    # Question input
    query = st.text_input("Ask a Question")
    if query:
        try:
            # Create embeddings
            embeddings = OpenAIEmbeddings(api_key=api_key)
            vectorstore = FAISS.from_documents(texts, embeddings)

            # LLM + QA Chain
            llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo", api_key=api_key)
            chain = load_qa_chain(llm, chain_type="stuff")

            # Run chain
            docs = vectorstore.similarity_search(query)
            st.write("Top matching chunk(s):")
            for i, doc in enumerate(docs):
                st.write(f"Chunk {i+1}:", doc.page_content[:500])
            answer = chain.run(input_documents=docs, question=query)

            st.subheader("📌 Answer")
            st.write(answer)

        except Exception as e:
            st.error(f"⚠️ Error: {e}")
