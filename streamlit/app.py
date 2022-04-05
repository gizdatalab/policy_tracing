import analyse_site
import main_site
import check_site
from multiapp import MultiApp
import streamlit as st

st.set_page_config(f'SDSN x GIZ Policy Tracing', layout="wide")

app = MultiApp()

app.add_app("SDSN X GIZ Policy Tracing", main_site.app)
app.add_app("Analyse Policy Document", analyse_site.app)
app.add_app("Check Coherence", check_site.app)

app.run()