import streamlit as st
import requests
import pandas as pd

st.title("Error Log")

response = requests.get(
    "http://127.0.0.1:8000/errors"
)

error_data = response.json()

df = pd.DataFrame(error_data)

# Remove unnecessary columns
df = df.drop(
    columns=["id", "row_num"],
    errors="ignore"
)

# Rename for better readability
df = df.rename(
    columns={
        "file_name": "File Name",
        "error_type": "Error Type",
        "error_message": "Error Message",
        "created_at": "Created At"
    }
)

st.write(
    f"Total Validation Errors : {len(df)}"
)

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)