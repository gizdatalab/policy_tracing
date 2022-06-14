import streamlit as st

import glob, os, sys; sys.path.append('../src')
#import helper
import preprocessing as pre
import cleaning as clean

def app():
    # Sidebar
    st.sidebar.title('Analyse Policy Document')

    # Container
    with st.container():
        st.markdown("<h1 style='text-align: center; color: black;'>SDSN X GIZ Policy Tracing</h1>",
                    unsafe_allow_html=True)

        file = st.file_uploader('Upload PDF File', type=['pdf', 'docx', 'txt'])

        if file is not None:
            st.write("Filename: ", file.name)
            # text = []
            # with pdfplumber.open(file) as pdf:
            #     for page in pdf.pages:
            #         text.append(page.extract_text())
            #     text_str = ' '.join([page for page in text])

            #     st.write('Number of pages:',len(pdf.pages))

            # load document
            docs = pre.load_document(file)

            # preprocess document
            docs_processed, df, all_text = clean.preprocessing(docs)
                

        
            st.write('... ')

        else:
            st.write(' ')
            st.write(' ')
            st.markdown("<h3 style='text-align: center; color: black;'>no PDF uploaded ...</h3>",
                        unsafe_allow_html=True)
