import streamlit as st
import requests
import pandas as pd

st.title("👨‍💼 Employee Records")

response = requests.get(
    "http://127.0.0.1:8000/employees"
)

employees = response.json()

df = pd.DataFrame(employees)

st.write(
    f"Total Employees Loaded : {len(df)}"
)

st.dataframe(
    df,
    use_container_width=True
)