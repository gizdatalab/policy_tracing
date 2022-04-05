import streamlit as st


def app():

    with st.container():
        st.markdown("<h1 style='text-align: center; color: black;'>SDSN X GIZ Policy Tracing</h1>", unsafe_allow_html=True)
        st.write(' ')
        st.write(' ')
        c1, c2, c3 = st.columns([1,7,1])

        c2.image("https://sustainability.yale.edu/sites/default/files/resize/images/paris_3obj_infographic%20%281%29-800x447"
                 ".png", width=1000)