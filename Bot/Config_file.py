import streamlit as st


def config_file():
    file = st.file_uploader("Upload your Config File", type='txt')
    return file
