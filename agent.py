#加载LangSmith
import os
os.environ["LANGCHAIN_TRACING_V2"] = ""
os.environ["LANGCHAIN_API_KEY"] = ""
os.environ["LANGCHAIN_PROJECT"] = ""
os.environ["SERPAPI_API_KEY"] = "<your SPER API KEY>"
#加载自定义工具
from Mytools import *
from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver
SYSTEM_PROMPT="""

"""
def load_chain():
    llm = ChatOllama(model="qwen2:7b")
    checkpointer = MemorySaver()
    prompt = ChatPromptTemplate.from_messages([
    ("system",SYSTEM_PROMPT),
    ("placeholder","{messages}")
    ])

    tools = [search,from_pdf_search]
    agent = create_react_agent(model=llm,tools=tools,prompt=prompt,checkpointer=checkpointer)
    
    return agent