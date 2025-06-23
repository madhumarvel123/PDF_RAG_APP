# Ask Your PDF – AI-Powered Q&A App

This app lets you upload a PDF and ask any question about its content. It uses OpenAI GPT model along with LangChain and FAISS to read and search through the document intelligently. Built with Streamlit.

---

## 🔍 What it does

- Upload any text-based PDF file  
- Reads and processes the content automatically  
- Lets you ask questions in plain English  
- Uses AI to find and answer based on the document  
- Preview of extracted text is shown  

---

## 🛠 How to run locally

### 1. Clone the project
```bash
git clone https://github.com/madhumarvel123/PDF_RAG_APP.git
cd PDF_RAG_APP
```

### 2. Install the required packages
```bash
pip install -r requirements.txt
```

### 3. Add your OpenAI API Key
Create a `.env` file in the root folder and paste:
```
OPENAI_API_KEY=your_openai_api_key_here
```

### 4. Run the Streamlit app
```bash
streamlit run app.py
```

---

## ⚙️ Tech stack used

- **Streamlit** – user interface  
- **LangChain** – handles chunking and retrieval  
- **FAISS** – vector store for semantic search  
- **OpenAI GPT-3.5** – for answering questions  
- **PyPDF2 / unstructured** – to read and parse PDF content  

---

## 📁 Project structure

```
📦 PDF_RAG_APP
├── app.py              # Streamlit app logic
├── requirements.txt    # Required Python packages
├── .env                # API key (not included in repo)
├── .gitignore          # Ignore temp files and secrets
└── temp/               # Temp files stored here
```

---

## 🤖 What kind of questions can I ask?

- What is this paper about?  
- What are the key findings?  
- What methods were used?  
- Who are the authors?  
- What is the conclusion?  

---

## ⚠️ Notes

- Works best with clean, text-based PDFs  
- Avoid scanned/image PDFs (they don’t extract text well)  
- Don’t share your `.env` or API key publicly  
- The output may vary depending on PDF formatting and size  

