import streamlit as st
import requests

st.title(
    "Dashboard Summary"
)

response = requests.get(
    "http://127.0.0.1:8000/dashboard-summary"
)

data = response.json()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Unique Employees",
        data["unique_employees"]
    )

with col2:
    st.metric(
        "Files Processed",
        data["files_processed"]
    )

with col3:
    st.metric(
        "Errors",
        data["total_errors"]
    )

col4, col5, col6 = st.columns(3)

with col4:
    st.metric(
        "Rows Read",
        data["total_rows_read"]
    )

with col5:
    st.metric(
        "Valid Records",
        data["valid_records"]
    )

with col6:
    st.metric(
        "Duplicates",
        data["duplicate_records"]
    )