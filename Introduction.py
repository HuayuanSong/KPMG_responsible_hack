import streamlit as st

# from streamlit_extras.app_logo import add_logo
from streamlit import session_state as session

# Configure Streamlit page
st.set_page_config(page_title="NLP POC💡", page_icon="💡")
# add_logo("logo.png", height=300)
st.title("NLP POC for KPMG Responsible AI Hackathon 2023💡")
st.markdown(
    """Welcome to the POC Demo for KPMG's Responsible AI Hackathon in developing an ESG compliant solution. This is a small collection of use-cases, 
    where we have applied different Natural Language Processing and 
    Machine Learning technologies to showcase how to create applicable AI to the benefit of people."""
)
