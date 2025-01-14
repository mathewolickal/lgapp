from langchain_openai import ChatOpenAI
import streamlit as st
from langchain.prompts import PromptTemplate

st.title("Ask the dosage/direction that needs to be converted")

with st.sidebar:
        st.title("Provide your API Key")
        OPENAI_API_KEY = st.text_input("OpenAI API key",type="password")



if not OPENAI_API_KEY:
    st.info("Enter your OpenAI API key to Continue")
    st.stop()

llm = ChatOpenAI(model="gpt-4o", api_key=OPENAI_API_KEY)

prompt_template = PromptTemplate(
    input_variables=["question"],
    template= """ You are an expert in giving the SIG code value from a dosage Direction.
     Only provide the SIG Value. Avoid giving information if the input is not clear and answer:I dont know
     Answer the question: What is the SIG code for{question}?
     """
)

question = st.text_input("Enter the Dosage/Direction")

if question:
    #response = llm.invoke(question)
    response = llm.invoke(prompt_template.format(question=question))
    st.write(response.content)
