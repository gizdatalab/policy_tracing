import streamlit as st


def app():

    with st.container():
        st.markdown("<h1 style='text-align: center; color: black;'>SDSN X GIZ Policy Tracing</h1>", unsafe_allow_html=True)
        st.write(' ')
        st.write(' ')
        c1, c2, c3 = st.columns([1,5,1])

        c2.image("https://sustainability.yale.edu/sites/default/files/resize/images/paris_3obj_infographic%20%281%29-800x447"
                 ".png", width=1000)
            
    with st.expander("ℹ️ - About this app", expanded=True):

        st.write(
            """     
    -   The *BERT Keyword Extractor* app is an easy-to-use interface built in Streamlit for the amazing [KeyBERT](https://github.com/MaartenGr/KeyBERT) library from Maarten Grootendorst!
    -   It uses a minimal keyword extraction technique that leverages multiple NLP embeddings and relies on [Transformers] (https://huggingface.co/transformers/) 🤗 to create keywords/keyphrases that are most similar to a document.
            """
        )

        st.markdown("")

    st.markdown("")
    st.markdown("## **📌 Paste document **")