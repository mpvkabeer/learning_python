import streamlit as st
from langchain_ollama import ChatOllama

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
        local_model = "llama3"
        llm = ChatOllama(model=local_model, temperature=0.7)

        stream = llm.stream(
            input=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ]
        )

        response = st.write_stream(stream)

    st.session_state.messages.append({"role": "assistant", "content": response})
