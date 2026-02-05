from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()

# Make sure you have HUGGINGFACEHUB_API_TOKEN in your .env file
# Get your free API token from: https://huggingface.co/settings/tokens

st.header("Research Tool")

user_input = st.text_input("Enter your research query here:")
if st.button("submit"):
        client = InferenceClient(token=os.getenv("HUGGINGFACEHUB_API_TOKEN"))
        response = client.chat_completion(
                messages=[{"role": "user", "content": user_input}],
                model="mistralai/Mistral-7B-Instruct-v0.3",
                max_tokens=500
        )
        st.write("Response:")
        st.write(response.choices[0].message.content)