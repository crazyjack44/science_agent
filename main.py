from agent import load_chain
import gradio as gr
from Mytools import *
SYSTEM_PROMPT="""

"""
chain = load_chain()
def agent_answer(question: str, history):
    """
    调用问答链进行回答
    """
    print(question)
    if question == None or len(question) < 1:
        return ""
    try:
        response = chain.invoke({"messages": [("user",question)]},
config={"configurable": {"thread_id": 42}})

        # 将问答结果直接附加到问答历史中， Gradio会将其展示出来
        return response["messages"][-1].content
    except Exception as e:
        return e

demo = gr.ChatInterface(
    fn=agent_answer,
    type="messages",
    title="本地科研助理",
    description="<center>基于QWen2</center>",
)
demo.launch()


