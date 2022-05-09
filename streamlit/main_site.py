import streamlit as st
from keybert import KeyBERT
import seaborn as sns

def app():

    with st.container():
        st.markdown("<h1 style='text-align: center; color: black;'>SDSN X GIZ Policy Tracing</h1>", unsafe_allow_html=True)
        st.write(' ')
        st.write(' ')
        c1, c2, c3 = st.columns([1,5,1])

        c2.image("https://sustainability.yale.edu/sites/default/files/resize/images/paris_3obj_infographic%20%281%29-800x447"
                 ".png", width=500)
            
    with st.expander("ℹ️ - About this app", expanded=True):

        st.write(
            """     
    -   The *Policy Action Tracker* app is an easy-to-use interface built in Streamlit for the amazing [KeyBERT](https://github.com/MaartenGr/KeyBERT) library from Maarten Grootendorst!
    -   It uses a minimal keyword extraction technique that leverages multiple NLP embeddings and relies on [Transformers] (https://huggingface.co/transformers/) 🤗 to create keywords/keyphrases that are most similar to a document.
            """
        )

        st.markdown("")

    st.markdown("")
    st.markdown("## **📌 Upload document **")
    
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

            @st.cache(allow_output_mutation=True)
            def load_model():
                return KeyBERT(model=roberta)

            kw_model = load_model()

            keywords = kw_model.extract_keywords(
            text,
            keyphrase_ngram_range=(1, 3),
            use_mmr=True,
            stop_words="english",
            top_n=10,
            diversity=0.5,
            )

            st.markdown("## **🎈 Check & download results **")

            df = (
                DataFrame(keywords, columns=["Keyword/Keyphrase", "Relevancy"])
                .sort_values(by="Relevancy", ascending=False)
                .reset_index(drop=True)
            )

            df.index += 1

            # Add styling
            cmGreen = sns.light_palette("green", as_cmap=True)
            cmRed = sns.light_palette("red", as_cmap=True)
            df = df.style.background_gradient(
                cmap=cmGreen,
                subset=[
                    "Relevancy",
                ],
            )
            c1, c2, c3 = st.columns([1, 3, 1])

            format_dictionary = {
                "Relevancy": "{:.1%}",
            }

            df = df.format(format_dictionary)

            with c2:
                st.table(df)


