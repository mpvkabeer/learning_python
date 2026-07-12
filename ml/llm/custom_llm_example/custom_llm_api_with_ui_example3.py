import streamlit as st
from langchain_ollama import ChatOllama
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')

import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.llms import Ollama
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings

directory = './custom_models/'
all_documents = []

for filename in os.listdir(directory):
    if filename.endswith('.pdf'):
        filepath = os.path.join(directory, filename)
        loader = PyPDFLoader(filepath)
        documents = loader.load()
        all_documents.extend(documents)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
texts = text_splitter.split_documents(all_documents)

embeddings = OllamaEmbeddings(model="nomic-embed-text")

#vectorstore = Chroma.from_texts(texts, embedding=embeddings)

if os.path.exists('chroma_db'):
    # Load
    vectorstore = Chroma(embedding_function=embeddings, persist_directory="chroma_db")
else:
    # If not found -> throw error -> create new
    vectorstore = Chroma.from_documents(texts, embeddings, persist_directory="chroma_db")


retriever = vectorstore.as_retriever()

history = []

# 3. Define the Prompt Template
template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

st.title("My Smart Bot 💬")
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if query := st.chat_input("Write your queries here"):
    st.session_state.messages.append({"role": "user", "content": query})

    with st.chat_message("user"):
        st.markdown(query)

    with st.chat_message("assistant"):
        #local_model = "llama3.1"
        local_model = "llama3"

        llm = ChatOllama(model=local_model, temperature=0.2)

        # llm = ChatOllama(model=local_model, temperature=0.7)
        # if prompt.lower() in ["quit","exit","bye"]:
        #     result = "Bot: Goodbye!"

        history.append({"role": "user", "content": HumanMessage(content=query)})

        print(f"query: {query}")

        rag_chain = (
                {"context": retriever, "question": RunnablePassthrough()}
                | prompt
                | llm
                | StrOutputParser()
        )

    response = rag_chain.invoke(query)

    st.session_state.messages.append({"role": "assistant", "content": response})
