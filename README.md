# Industry Report Assistant 📊

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ai-industry-analyst.streamlit.app/)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repo-blue?logo=github)](https://github.com/daifayo7/ai-industry-analyst)

An AI-powered tool that generates professional industry report summaries with a streaming (typewriter) effect. Built with [Streamlit](https://streamlit.io/) and [Groq](https://groq.com/) for fast, real-time output.

**👉 [Try it live](https://ai-industry-analyst.streamlit.app/)** – no installation required!

---

## Features

- Enter any industry or topic, get a concise report summary  
- Real-time streaming output (character-by-character)  
- Powered by Groq's high-speed inference  
- Simple web interface, deployable with one click  

---

## Quick Start (Local)

### 1. Clone the repository
```bash
git clone https://github.com/daifayo7/ai-industry-analyst.git
cd ai-industry-analyst
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set your Groq API key
Create a free API key at [console.groq.com](https://console.groq.com/), then export it:
```bash
export GROQ_API_KEY="your-api-key"
```

### 4. Run the app
```bash
streamlit run app.py
```
The app will open in your browser at `http://localhost:8501`.

---

## Deploy to Streamlit Cloud

1. Push this repository to GitHub.
2. Log in to [share.streamlit.io](https://share.streamlit.io) with your GitHub account.
3. Click **New app**, select your repo, branch (`main`), and main file (`app.py`).
4. In **Advanced settings**, add a secret:
   ```
   GROQ_API_KEY = your-api-key
   ```
5. Click **Deploy**. Your app will be live at `https://your-app-name.streamlit.app`.

---

## Notes

- **Model updates**: Groq's free models are updated occasionally. If you see a `model_decommissioned` error, run `check_models.py` (or the script below) to list available models and update the `model` parameter in `app.py`:
  ```python
  from groq import Groq
  import os
  client = Groq(api_key=os.getenv("GROQ_API_KEY"))
  for m in client.models.list().data:
      print(m.id)
  ```
- **Input length**: The default model `llama-3.3-70b-instruct` supports about 8192 tokens. For longer inputs, use `mixtral-8x7b-32768` (32k tokens).

---

## License

MIT

---

## 中文简介

一个基于 Groq 和 Streamlit 的行业报告生成工具，支持流式输出。

- 输入行业或主题，自动生成专业报告摘要  
- 打字机效果逐字输出  
- 在线体验：[https://ai-industry-analyst.streamlit.app/](https://ai-industry-analyst.streamlit.app/)

### 本地运行步骤

1. 克隆仓库  
2. 安装依赖：`pip install -r requirements.txt`  
3. 设置环境变量：`export GROQ_API_KEY="你的密钥"`  
4. 运行：`streamlit run app.py`

### 部署到 Streamlit Cloud

在平台中添加 `GROQ_API_KEY` 密钥即可一键部署。