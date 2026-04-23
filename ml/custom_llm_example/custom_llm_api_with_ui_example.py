import streamlit as st
from langchain_ollama import ChatOllama

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

def docx_to_text(document):
    texts = []
    for page in document:
        texts.append(page.page_content)
    return '\n'.join(texts)

for filename in os.listdir(directory):
    if filename.endswith('.pdf'):
        filepath = os.path.join(directory, filename)
        loader = PyPDFLoader(filepath)
        documents = loader.load()
        all_documents.extend(docx_to_text(documents))

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
texts = text_splitter.split_text( '\n'.join(all_documents))

embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
#embeddings = SentenceTransformerEmbeddings(model_name="llama3")

vectorstore = Chroma.from_texts(texts, embedding=embeddings)

system_prompt = "Auto Response"

qa_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    )

retriever = vectorstore.as_retriever()
history = []

st.title("My Smart Bot 💬")
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Write your queries here"):
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        #local_model = "llama3.1"
        #local_model = "llama3"

        # llm = ChatOllama(model=local_model, temperature=0.2)
        llm = Ollama(model="phi3.5")

        # llm = ChatOllama(model=local_model, temperature=0.7)
        # if prompt.lower() in ["quit","exit","bye"]:
        #     result = "Bot: Goodbye!"

        history.append({"role": "user", "content": HumanMessage(content=prompt)})

        print(f"prompt: {prompt}")
        if prompt:
            relevant_docs = retriever.invoke(prompt)
            context_documents_str = "\n\n".join(doc.page_content for doc in relevant_docs)
        else:
            context_documents_str = ""

        print(f"context_documents_str: {context_documents_str}")

        qa_prompt_local  = qa_prompt.partial(
            history=history,
            context=context_documents_str
        )

        llm_chain = { "input": RunnablePassthrough() } | qa_prompt_local  | llm

        #result = llm_chain.invoke(prompt)
        result = llm_chain.invoke(prompt)

        # stream = llm_chain.stream(
        #     input=[
        #         {"role": m["role"], "content": m["content"]}
        #         for m in st.session_state.messages
        #     ]
        # )

        # response = st.write_stream(stream)
        response = st.write(result)

    st.session_state.messages.append({"role": "assistant", "content": response})
