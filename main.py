import streamlit as st
from streamlit_option_menu import option_menu
import importlib

PAGES = {
    "Home": "streamlit_app.home",
    "Calculus": "streamlit_app.calculus.index",
    "Electronics": "streamlit_app.microelectronic.index"
}

st.set_page_config(page_title="Embedded Journey", layout="wide")

st.sidebar.title("Navegação")
selection = st.sidebar.radio("Ir para", list(PAGES.keys()))

module = importlib.import_module(PAGES[selection])
module.app()
