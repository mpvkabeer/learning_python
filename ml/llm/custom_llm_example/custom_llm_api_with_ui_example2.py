from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

# 1. Setup Models (Ollama)
llm = ChatOllama(model="llama3")
embeddings = OllamaEmbeddings(model="nomic-embed-text")

# 2. Setup Vector Store & Retriever
# Note: In a real app, you would load and split your documents first
texts = ["The capital of France is Paris.", "The Eiffel Tower is in Paris."]
vectorstore = Chroma.from_texts(texts, embedding=embeddings)
retriever = vectorstore.as_retriever()

# 3. Define the Prompt Template
template = """Answer the question based only on the following context:
{context}

Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

# 4. Construct the LCEL Chain
# This chain:
# a) Takes the user question
# b) Retrieves context in parallel (RunnablePassthrough/retriever)
# c) Passes formatted context + question to the prompt
# d) Sends the prompt to the LLM
# e) Parses the final string output
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}

    | prompt
    | llm
    | StrOutputParser()
)

# 5. Execute
response = rag_chain.invoke("What is the capital of France?")
print(response)
