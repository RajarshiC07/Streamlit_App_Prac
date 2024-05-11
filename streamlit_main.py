import streamlit as st
from langchain.llms import HuggingFaceHub

import time

ENDPOINT_URL = "satvikag/chatbot"

LLM = HuggingFaceHub(repo_id = ENDPOINT_URL, huggingfacehub_api_token = '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', model_kwargs={"temperature":1})

with st.sidebar:
    messages = st.container(height=300)
    if prompt := st.chat_input("Say something"):
        messages.chat_message("user").write(prompt)
        output = None
        print(prompt)
        while output is None:
            try:
                output = LLM.invoke(prompt)
            except Exception as err:
                with st.status("Typing..."):
                    time.sleep(2)
        messages.chat_message("assistant").write(f"Echo: {output}")
