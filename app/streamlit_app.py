import streamlit as st
from pymongo import MongoClient
import pandas as pd

client = MongoClient("mongodb+srv://sonu74swami_db_user:7X7fqpda64VeptLT@cluster0.dphf6kj.mongodb.net/")
db = client["b2b_db"]
collection = db["companies"]

st.title("🚀 B2B Lead Intelligence Dashboard")

# Fetch data
try:
    data = list(collection.find({}, {"_id": 0}))
except Exception as e:
    st.error(f"Database error: {e}")
    data = []

df = pd.DataFrame(data)

st.write("📊 Total Records:", len(df))

if df.empty:
    st.warning("⚠️ No data found. Run pipeline first.")
else:
    search = st.text_input("🔍 Search")

    if search and "name" in df.columns:
        df = df[df["name"].astype(str).str.contains(search, case=False, na=False)]

    st.dataframe(df)