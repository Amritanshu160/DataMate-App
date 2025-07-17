import streamlit as st
import pandas as pd
import sqlite3
from google import genai
from decouple import config
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# Streamlit App
st.set_page_config(page_title="Text-to-SQL App", page_icon="📊", layout="wide")
st.title("📊 Text-to-SQL Query Generator using Gemini")

uploaded_file = st.file_uploader("Upload your CSV dataset", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("📊 Preview of Dataset")
    st.dataframe(df.head())

    # Load to in-memory SQLite DB
    conn = sqlite3.connect(":memory:")
    df.to_sql("data", conn, index=False, if_exists="replace")

    st.markdown("#### 🤖 Ask a question (in natural language)")
    user_query = st.text_input("For example: 'Show all employees with salary > 50000'")

    if st.button("Generate & Run SQL") and user_query:
        # Prepare prompt for Gemini
        prompt = f"""
        You are a helpful assistant. Convert the natural language query to an SQL query.
        Use the table name: data
        Here is the schema:
        {str(df.dtypes)}

        Question: {user_query}

        Return only the SQL query without explanation.
                """

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
            sql_query = response.text.strip().strip("```sql").strip("```")
            st.code(sql_query, language="sql")

            # Run SQL Query
            try:
                result = pd.read_sql_query(sql_query, conn)
                st.success("✅ Query executed successfully!")
                st.dataframe(result)
            except Exception as e:
                st.error(f"⚠️ Error executing SQL: {e}")

        except Exception as e:
            st.error(f"⚠️ Error generating SQL with Gemini: {e}")
