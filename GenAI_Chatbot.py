api_key = "YOUR_API_KEY"

from groq import Groq
import streamlit as st
from dotenv import load_dotenv
import os


llm = Groq(api_key=api_key)

st.subheader("Groq QnA Bot")
query = st.chat_input(
    placeholder="Ask me anything..."
)

if query:
    st.chat_message("user").markdown(query)

    res = llm.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role":"user",
                "content":query
            }
        ]
)


    finalAnswer = res.choices[0].message.content
    st.chat_message("ai").markdown(finalAnswer)

