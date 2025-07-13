import streamlit as st
from streamlit_option_menu import option_menu
import importlib
import pandas as pd

PAGES = {
    "Home": "streamlit_app.home",
    "Calculus": "streamlit_app.calculus.index",
    "Electronics": "streamlit_app.microelectronic.index"
}

chart_data = pd.DataFrame(
    data=[
        [1, 7, 4],
        [2, 8, 5],
        [3, 9, 6]
    ],
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

st.set_page_config(page_title="Embedded Journey", layout="wide")

st.sidebar.title("Navegação")
selection = st.sidebar.radio("Ir para", list(PAGES.keys()))

module = importlib.import_module(PAGES[selection])
module.app()
