# 行业报告助手

import streamlit as st
import os
from langchain_groq import ChatGroq


# 设置页面标题
st.set_page_config(page_title="行业报告助手",page_icon="🤖")
st.title("🤖行业报告助手")
st.write("输入行业或主题，AI 将逐字生成专业报告摘要或分析")



# 直接创建 ChatGroq 实例
llm = ChatGroq(
    model = "groq/compound-mini",
    temperature=0.7,
    api_key=os.getenv("GROQ_API_KEY")  # 从环境变量读取
)



# 用户输入
user_input = st.text_input("请输入行业或报告主题：",placeholder="例如：2026年全球AI芯片市场分析")
if user_input:
    st.markdown(f"**您的问题：** {user_input}")

    answer_placeholder = st.empty()
    full_response = ""

    # 流式输出
    for chunk in llm.stream(user_input):
        full_response += chunk.content
        answer_placeholder.markdown(f"**报告内容：** {full_response}▌")

    # 最终输出（去掉光标）
    answer_placeholder.markdown(f"**报告内容：** {full_response}")