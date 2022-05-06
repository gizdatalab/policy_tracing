import pdfminer
from pdfminer.high_level import extract_pages
import streamlit as st
from io import StringIO
import base64
import pdfplumber



def app():
    # Sidebar
    st.sidebar.title('Analyse Policy Document')

    # Container
    with st.container():
        st.markdown("<h1 style='text-align: center; color: black;'>SDSN X GIZ Policy Tracing</h1>",
                    unsafe_allow_html=True)
        file = st.file_uploader('Upload', type=['pdf'])
        


        if file is not None:
            with pdfplumber.open(file) as pdf:
                pages = pdf.pages[0]
                st.write(pages.extract_text())

        
            st.write('... ')

        else:
            st.write(' ')
            st.write(' ')
            st.markdown("<h1 style='text-align: center; color: black;'>no PDF uploaded ...</h1>",
                        unsafe_allow_html=True)
