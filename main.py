# main.py
# AmbedkarGPT – RAG using LangChain + Chroma + HuggingFace + Ollama llama3.2:1b

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_ollama import OllamaLLM
import shutil
import os


# -------------------------------------------------------------------
# DELETE OLD VECTOR DATABASE
# -------------------------------------------------------------------
def reset_vector_db():
    if os.path.exists("chroma_db"):
        shutil.rmtree("chroma_db")
        print("[✔] Old vector DB deleted.")
    else:
        print("[✔] No previous vector DB found.")


# -------------------------------------------------------------------
# BUILD NEW VECTOR STORE
# -------------------------------------------------------------------
def build_vector_db():
    print("[1] Loading speech.txt ...")
    loader = TextLoader("speech.txt")
    docs = loader.load()

    print("[2] Splitting text into chunks ...")
    splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=30)
    chunks = splitter.split_documents(docs)

    print("[3] Creating embeddings ...")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    print("[4] Building Chroma vector DB ...")
    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="chroma_db"
    )

    print("[✔] New vector DB created.")
    return vectordb


# -------------------------------------------------------------------
# RAG FUNCTION
# -------------------------------------------------------------------
def rag(question, retriever, llm):
    docs = retriever.invoke(question)
    context = "\n".join([d.page_content for d in docs])

    prompt = f"""
Answer the question ONLY using the context below.
If answer not found in context, say "Not found in speech."

### CONTEXT:
{context}

### QUESTION:
{question}

### ANSWER:
"""

    return llm.invoke(prompt), docs


# -------------------------------------------------------------------
# MAIN
# -------------------------------------------------------------------
def main():
    # Always create a new DB
    reset_vector_db()

    vectordb = build_vector_db()
    retriever = vectordb.as_retriever(search_kwargs={"k": 2})

    print("[5] Loading Ollama model: llama3.2:1b ...")
    llm = OllamaLLM(model="llama3.2:1b")

    print("\n=========================================")
    print(" AmbedkarGPT — Using llama3.2:1b (FAST)")
    print(" Ask questions about the speech.")
    print(" Type 'exit' to quit.")
    print("==========================================\n")

    while True:
        question = input("You: ")
        if question.lower() == "exit":
            print("Goodbye!")
            break

        answer, sources = rag(question, retriever, llm)

        print("\nAnswer:", answer.strip())
        print("\n--- Sources Used ---")
        for s in sources:
            print("-", s.page_content)
        print()


if __name__ == "__main__":
    main()

