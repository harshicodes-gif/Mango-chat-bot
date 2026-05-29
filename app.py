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
        "gemini-2.0-flash"
    )

except Exception as e:
    st.error(
        f"Setup Error: {str(e)}"
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

# Display previous messages
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

    # Save user message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    # Show user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate response
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                # Build conversation context
                conversation = ""

                for msg in st.session_state.messages:

                    role = msg["role"]

                    if role == "assistant":
                        role = "AI"

                    conversation += (
                        f"{role}: {msg['content']}\n"
                    )

                response = model.generate_content(
                    conversation
                )

                reply = response.text

            except Exception as e:

                reply = (
                    "Sorry — something went wrong."
                )

                st.error(str(e))

            st.markdown(reply)

    # Save assistant message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )

