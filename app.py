import streamlit as st
from groq import Groq
from tavily import TavilyClient

st.set_page_config(
    page_title="Mango AI",
    page_icon="🥭",
    layout="centered"
)

st.title("🥭 Mango AI")
st.caption("AI with live web access")

try:
    client = Groq(
        api_key=st.secrets["GROQ_API_KEY"]
    )

    tavily = TavilyClient(
        api_key=st.secrets["TAVILY_API_KEY"]
    )

except Exception as e:
    st.error(str(e))
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hey! I'm Mango AI. Ask me anything."
        }
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Type your message...")

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

                search_results = tavily.search(
                    query=prompt,
                    search_depth="basic",
                    max_results=5
                )

                context = ""

                for result in search_results["results"]:

                    context += (
                        f"Title: {result['title']}\n"
                        f"Content: {result['content']}\n\n"
                    )

                messages = [
                    {
                        "role": "system",
                        "content":
                        "Use web results when relevant."
                    },
                    {
                        "role": "user",
                        "content":
                        f"""
Question:
{prompt}

Web Results:
{context}
"""
                    }
                ]

                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=messages
                )

                reply = (
                    response
                    .choices[0]
                    .message
                    .content
                )

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
