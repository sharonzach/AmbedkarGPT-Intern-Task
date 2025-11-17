# AmbedkarGPT-Intern-Task

A simple Retrieval-Augmented Generation (RAG) prototype built for the **Kalpit Pvt Ltd – AI Intern Hiring Assignment**.  
The system loads a speech by Dr. B.R. Ambedkar, creates embeddings, stores them in a local vector database, retrieves the most relevant chunks based on a user query, and generates an answer using a **local Ollama model (llama3.2:1b)**.

This solution runs **fully offline** using:
- LangChain (latest modular version)
- ChromaDB (local vector store)
- HuggingFace MiniLM embeddings
- Ollama (model: `llama3.2:1b` — very lightweight and works on low RAM)
- Python 3.8+ (WSL recommended on Windows)

---

## 🚀 Features

- Loads and processes `speech.txt`
- Splits speech into semantic chunks
- Generates embeddings using HuggingFace MiniLM
- Stores embeddings in ChromaDB
- Retrieves relevant chunks from the vector DB
- Uses **Ollama llama3.2:1b** to answer questions
- Fully local (no API keys, no cloud services)

---

## 📁 Project Structure

AmbedkarGPT-Intern-Task/
│── main.py
│── speech.txt
│── requirements.txt
└── README.md

---

## 🧠 Model Used

Why this model?  
✔ Very lightweight (~1B parameters)  
✔ Only ~1.2GB RAM needed  
✔ Works smoothly inside WSL on low-memory systems  
✔ Fast inference compared to Mistral 7B  

---

## ⚙️ Installation Instructions

### 1️⃣ Install WSL (Windows Users Only)

Open **PowerShell (Admin)**:


Restart PC → Open Ubuntu.

---

### 2️⃣ Install Ollama inside WSL

curl -fsSL https://ollama.ai/install.sh
 | sh

Then pull the lightweight model:

ollama pull llama3.2:1b

Test:

ollama run llama3.2:1b

---

### 3️⃣ Create and Activate a Python Virtual Environment

python3 -m venv venv
source venv/bin/activate


---

### 4️⃣ Install Dependencies

pip install -r requirements.txt

---

## ▶️ Running the Application

Inside the project folder:

python3 main.py


You will see:

AmbedkarGPT — Using llama3.2:1b
Ask questions about the speech.

Example:

**You:**  
What is the real remedy?

**Answer:**  
A correct context-based response from the text.

---

## 🔁 Rebuilding the Vector DB (Optional)

If you want to delete old DB and regenerate fresh vectors:

rm -rf chroma_db
python3 main.py

---

## 📄 Provided Speech Text (speech.txt)

This project uses the provided excerpt from **Annihilation of Caste**.

---

## ❗ Important Notes

- This is a **prototype**, not a production system.
- All processing is local — there is **no cloud**, **no API key**, and **no paid tools**.
- Optimized for low-RAM laptops using a small LLM.

---

## ✔ Submission Deliverables

Include in your GitHub repo:

- `main.py`
- `speech.txt`
- `requirements.txt`
- Updated `README.md`

Make your repository public and name it:


