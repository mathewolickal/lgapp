from langchain_openai import ChatOpenAI
import streamlit as st

from langchain.globals import set_debug

set_debug(True)

OPENAI_API_KEY = "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"

llm = ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY)
st.title("Ask Anything")

question = st.text_input("Enter the Dosage/Direction")

if question:
    response = llm.invoke(question)
    st.write(response.content)
