import pandas as pd
import os
import streamlit as st
from pandasai import SmartDataframe
from langchain_groq.chat_models import ChatGroq
from pandasai.responses.response_parser import ResponseParser

st.set_page_config(page_title="Chat with CSV",layout="wide", page_icon="💬")

# Initialize the language model
llm = ChatGroq(model_name="llama3-70b-8192", api_key="GROQ_API_KEY")

def load_data(uploaded_file) -> pd.DataFrame:
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        return data
    return None

class StreamlitResponse(ResponseParser):
    def format_dataframe(self, result):
        st.dataframe(result["value"])

    def format_plot(self, result):
        st.image(result["value"])

    def format_other(self, result):
        st.write(result["value"])

# Streamlit app title
st.write("# Chat with CSV Data 🦙")

# File uploader for CSV
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    df = load_data(uploaded_file)
    st.write(df)

    # Form to capture user input and submit
    with st.form(key="query_form"):
        query = st.text_area("🗣️ Chat with Dataframe", key="query_input")
        submit_button = st.form_submit_button(label="Generate")

    # Process the query when the form is submitted
    if submit_button and query:
        with st.spinner("Generating response..."):
            query_engine = SmartDataframe(df, config={"llm": llm, "response_parser": StreamlitResponse})
            answer = query_engine.chat(query)
            st.write(answer)
