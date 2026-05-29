import streamlit as st
from openai import OpenAI

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="Mango AI",
    page_icon="🥭",
    layout="centered"
)

# -----------------------------
# Styling
# -----------------------------
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

# -----------------------------
# Header
# -----------------------------
st.title("🥭 Mango AI")
st.caption("Clear and concise AI conversations.")

# -----------------------------
# OpenAI setup
# -----------------------------
try:
    api_key = st.secrets["OPENAI_API_KEY"]

    client = OpenAI(
        api_key=api_key
    )

except Exception:
    st.error(
        "Missing OpenAI API key. Add OPENAI_API_KEY in Streamlit Secrets."
    )
    st.stop()

# -----------------------------
# Chat History
# -----------------------------
if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hey! I'm Mango AI. How can I help you today?"
        }
    ]

# Display history
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# Input
# -----------------------------
prompt = st.chat_input(
    "Type your message..."
)

if prompt:

    # Store user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                response = client.chat.completions.create(
                    model="gpt-4.1-mini",
                    messages=st.session_state.messages
                )

                reply = response.choices[0].message.content

            except Exception as e:

                reply = (
                    "Sorry — something went wrong while "
                    "talking to OpenAI."
                )

                st.error(str(e))

            st.markdown(reply)

    # Save response
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )
