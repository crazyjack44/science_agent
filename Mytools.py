from langchain.agents import tool
from langchain_community.utilities import SerpAPIWrapper
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
#定义tools
#搜索工具
@tool
def search(query:str):
    """
    只有当需要了解实时信息或者不知道的事情的时候才会使用这个工具。
    """
    serp = SerpAPIWrapper()
    result = serp.run(query=query)
    print("搜索结果：",result)
    return result
#文档增强检索
@tool
def from_pdf_search(query:str):
    """
    当询问到和西南科技大学相关的知识点的时候，就使用这个工具。
    """ 
    persist_directory = 'faiss_index'
    embedding = HuggingFaceEmbeddings(model_name='./embeddings/bge-large-zh-v1.5')
    print("加载数据库")
    vector_db = FAISS.load_local(persist_directory,embedding_function=embedding)
    retriever=vector_db.as_retriever()
    result = retriever.get_relevant_documents(query)
    return result
