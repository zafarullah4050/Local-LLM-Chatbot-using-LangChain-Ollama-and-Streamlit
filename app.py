import os
from dotenv import load_dotenv
import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY", "")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT", "")


st.title("💬 Chat with Local LLM using Ollama")
prompt_input = st.text_input("Ask me anything...")


llm = Ollama(model="gemma:2b")  


prompt = ChatPromptTemplate.from_template("Q: {question} \nA:")


parser = StrOutputParser()

if prompt_input:
    chain = prompt | llm | parser
    response = chain.invoke({"question": prompt_input})
    st.write("**Answer:**", response)
