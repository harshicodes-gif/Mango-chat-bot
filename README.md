# Mango AI Chatbot 🥭

A simple AI chatbot built using Streamlit and Google Gemini.

## Features

- Conversational AI chatbot
- Built using Streamlit
- Powered by Gemini API
- Dark themed interface
- Maintains chat history
- Deployable on Streamlit Cloud

---

## Requirements

- Python 3.11 recommended
- Gemini API Key
- GitHub account (for deployment)
- Streamlit Cloud account

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

## Streamlit Deployment

1. Push your code to GitHub

```bash
git add .
git commit -m "deploy mango ai"
git push
```

2. Open Streamlit Cloud

3. Create a new app

4. Select your GitHub repository

5. Add Secrets:

```toml
GEMINI_API_KEY="YOUR_GEMINI_KEY"
```

6. Save secrets

7. Reboot app

---

## requirements.txt

```txt
streamlit>=1.35.0
google-generativeai>=0.8.0
```

---

## Troubleshooting

### API Key Error

Check:

```toml
GEMINI_API_KEY="YOUR_KEY"
```

### Model Errors

Make sure app.py uses:

```python
model = genai.GenerativeModel(
    "gemini-2.0-flash"
)
```

### Deployment Issues

- Reboot Streamlit app
- Verify Python version is 3.11
- Verify secrets are configured

---

## Tech Stack

- Streamlit
- Google Gemini API
- Python 3.11

---

## Author

Built with ❤️ by Harshita
