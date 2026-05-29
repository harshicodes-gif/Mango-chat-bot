import streamlit as st
import google.generativeai as genai

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
# Gemini setup
# -----------------------------
try:
    api_key = st.secrets["GEMINI_API_KEY"]

    genai.configure(
        api_key=api_key
    )

    model = genai.GenerativeModel(
        "gemini-1.5-flash"
    )

except Exception:
    st.error(
        "Missing GEMINI_API_KEY in Streamlit Secrets."
    )
    st.stop()

# -----------------------------
# Chat history
# -----------------------------
if "messages" not in st.session_state:

    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hey! I'm Mango AI. How can I help you today?"
        }
    ]

# Display messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -----------------------------
# User input
# -----------------------------
prompt = st.chat_input(
    "Type your message..."
)

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                response = model.generate_content(
                    prompt
                )

                reply = response.text

            except Exception as e:

                reply = (
                    "Sorry — something went wrong."
                )

                st.error(str(e))

            st.markdown(reply)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )
