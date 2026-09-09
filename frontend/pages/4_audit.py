import streamlit as st
import requests
import pandas as pd

st.title("Audit Log")

response = requests.get(
    "http://127.0.0.1:8000/audit"
)

df = pd.DataFrame(
    response.json()
)

st.dataframe(
    df,
    use_container_width=True
)