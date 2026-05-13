from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

from ai.huggingface_service import ask_huggingface

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = Chroma(
    persist_directory="rag/vector_store",
    embedding_function=embedding_model
)

retriever = vector_db.as_retriever(
    search_kwargs={"k": 3}
)

def rag_financial_chat(question):

    # docs = retriever.get_relevant_documents(question)
    docs = retriever.invoke(question)

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
    Use the following financial context to answer.

    Context:
    {context}

    Question:
    {question}

    Give a beginner-friendly financial explanation.
    """

    return ask_huggingface(prompt)

if __name__ == "__main__":

    answer = rag_financial_chat(
        "What are the benefits of SIP investing?"
    )

    print(answer)