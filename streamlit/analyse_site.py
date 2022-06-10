import streamlit as st
import pdfplumber

def app():
    # Sidebar
    st.sidebar.title('Analyse Policy Document')

    # Container
    with st.container():
        st.markdown("<h1 style='text-align: center; color: black;'>SDSN X GIZ Policy Tracing</h1>",
                    unsafe_allow_html=True)
        file = st.file_uploader('Upload PDF File', type=['pdf'])
        


        if file is not None:
            text = []
            with pdfplumber.open(file) as pdf:
                for page in pdf.pages:
                    text.append(page.extract_text())

                st.write('Number of pages:',len(pdf.pages))
                

        
            st.write('... ')

        else:
            st.write(' ')
            st.write(' ')
            st.markdown("<h3 style='text-align: center; color: black;'>no PDF uploaded ...</h3>",
                        unsafe_allow_html=True)
