import streamlit as st
from pymongo import MongoClient
import pandas as pd

client = MongoClient("mongodb://localhost:27017/")
db = client["b2b_db"]
collection = db["companies"]

st.title("🚀 B2B Lead Dashboard")

data = list(collection.find({}, {"_id": 0}))
df = pd.DataFrame(data)

search = st.text_input("Search Company")

if search:
    df = df[df["name"].str.contains(search, case=False)]

st.write(df)
st.write("Total:", len(df))