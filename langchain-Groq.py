# langchain是什么？
# 开发 ai agent 应用的框架
import os
from langchain_groq import ChatGroq

# 设置 groq 的 api key
llm = ChatGroq(
    model = "groq/compound-mini",
    temperature=0.7,
    api_key=os.getenv("GROQ_API_KEY")
)


response = llm.invoke("什么是RAG")
print(response)