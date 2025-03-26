import os
from dotenv import load_dotenv
from langchain_community.llms import Ollama
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_PROJECT'] = os.getenv('LANGCHAIN_PROJECT')
os.environ['LANGCHAIN_TRACING_V2'] = 'true'


prompt = ChatPromptTemplate.from_messages([
    ("system","You are a helpful AI assistant. Your name is Izu. Please respond to the question asked."),
    ("user","Question : {question}")
]
)

output_parser = StrOutputParser()
llm = Ollama(model="gemma3")
chain = prompt|llm|output_parser

st.title("Playing around with Gemma3👋")
input_text = st.text_input("What do you want to know about?")

if input_text:
    st.write(chain.invoke({'question':input_text}))