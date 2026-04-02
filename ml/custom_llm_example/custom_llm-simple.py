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

embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
#embeddings = SentenceTransformerEmbeddings(model_name="llama3")

if os.path.exists('chroma_db'):
    # Load
    vectorstore = Chroma(embedding_function=embeddings, persist_directory="chroma_db")
else:
    # If not found -> throw error -> create new
    vectorstore = Chroma.from_documents(texts, embeddings, persist_directory="chroma_db")

##llm = Ollama(model="phi3.5")
llm = Ollama(model="llama3")

system_prompt = "Auto Response"

qa_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    )

def chainingFunction():
    retriever = vectorstore.as_retriever()
    history = []

    while True:
        query = input("Question:")

        print("User:", query, "\n")
        if query.lower() in ["quit","exit","bye"]:
            print("Bot: Goodbye!")
            break

        history.append({"role": "user", "content": HumanMessage(content=query)})

        if query:
            relevant_docs = retriever.invoke(query)
            context_documents_str = "\n\n".join(doc.page_content for doc in relevant_docs)
        else:
            context_documents_str = ""

        qa_prompt_local  = qa_prompt.partial(
            history=history,
            context=context_documents_str
        )

        llm_chain = { "input": RunnablePassthrough() } | qa_prompt_local  | llm

        result = llm_chain.invoke(query)

        history.append({"role": "assistant", "content": AIMessage(content=result)})

        print("Bot:", result, "\n\n")

chainingFunction()