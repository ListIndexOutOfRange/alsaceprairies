import streamlit as st
from typing import List

def sidebar(pages: List[str]) -> st.radio:
    selection = st.sidebar.radio("Aller à", pages)
    return selection