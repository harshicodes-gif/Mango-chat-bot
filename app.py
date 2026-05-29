import streamlit as st
from openai import OpenAI

# Page configuration
st.set_page_config(
    page_title="Mango AI",
    page_icon="🥭",
    layout="centered"
)

# Custom styling
st.markdown("""
    <style>
    .stChatMessage {
        border-radius: 15px;
        padding: 10px;
    }

    .main {
        background-color: #0f1117;
    }

    h1 {
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🥭 Mango AI")
st.caption("Clear and concise AI conversations.")

# OpenAI client
client = OpenAI(
    api_key=st.secrets["OPENAI_API_KEY"]
)

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hey! I'm Mango AI. How can I help you today?"
        }
    ]

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
prompt = st.chat_input("Type your message...")

if prompt:

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=st.session_state.messages
            )

            reply = response.choices[0].message.content

            st.markdown(reply)

    # Save assistant response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )
