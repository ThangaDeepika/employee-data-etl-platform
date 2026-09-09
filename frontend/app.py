import streamlit as st

st.set_page_config(
    page_title="Employee ETL Dashboard",
    layout="wide"
)

st.title(
    "📊 Employee ETL Dashboard"
)

st.markdown(
    """
    ### Welcome

    Use the menu on the left to navigate:

    ✅ Dashboard Summary
    
    ✅ Employee Records
    
    ✅ Error Logs
    
    ✅ Audit Logs
    """
)