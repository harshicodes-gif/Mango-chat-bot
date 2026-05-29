# Mango AI Chatbot 🥭

A simple AI chatbot.

## Features

- Conversational AI chatbot
- Chat history support
- Powered by Groq LLMs
- Deployable on Streamlit Cloud
- Dark themed interface

---

## Requirements

- Python 3.11 recommended
- Groq API Key
- GitHub account
- Streamlit Cloud account

---

## Installation

Clone repository:

```bash
git clone YOUR_GITHUB_REPO_LINK
cd YOUR_PROJECT_FOLDER
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run locally:

```bash
streamlit run app.py
```

---

## Project Structure

```text
project/
│
├── app.py
├── requirements.txt
├── README.md
├── .devcontainer/
│   └── devcontainer.json
```

---

## Streamlit Deployment

Push changes:

```bash
git add .
git commit -m "deploy mango ai"
git push
```

Add secrets:

```toml
GROQ_API_KEY="YOUR_GROQ_KEY"
```

Reboot Streamlit app.

---

## Tech Stack

- Streamlit
- Groq API
- Python 3.11
