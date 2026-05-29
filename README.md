# Mango AI Chatbot 🥭

A chatbot application built by Harshita using Streamlit with support for conversational responses and live information retrieval.

## About The Project

Mango AI is a chatbot designed to answer questions, maintain conversation history, and retrieve recent information from the web when needed.

This project was built to explore:

* Conversational AI applications
* Real-time information retrieval
* Streamlit deployment workflows
* API integration and chatbot design

---

## Features

* Interactive chat interface
* Conversation history support
* Real-time information retrieval
* Simple and clean UI
* Deployable on Streamlit Cloud

---

## Requirements

* Python 3.11 recommended
* API keys for configured services
* GitHub account
* Streamlit Cloud account

---

## Installation

Clone the repository:

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

## Deployment

1. Push code to GitHub

```bash
git add .
git commit -m "deploy mango ai"
git push
```

2. Deploy using Streamlit Cloud

3. Add required secrets

```toml
GROQ_API_KEY="YOUR_KEY"
TAVILY_API_KEY="YOUR_KEY"
```

4. Reboot the application

---

## Future Improvements

* File uploads
* Voice interactions
* Better memory handling
* Improved UI customization
* Expanded search capabilities

---

## Author

Built by **Harshita**

