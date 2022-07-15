# set path
import glob, os, sys; sys.path.append('../src')

#import helper
import preprocessing as pre
import cleaning as clean

#import needed libraries
import seaborn as sns
from pandas import DataFrame
from keybert import KeyBERT
from transformers import pipeline
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import pandas as pd 

import tempfile
import sqlite3

def app():

    with st.container():
        st.markdown("<h1 style='text-align: center; color: black;'> Policy Action Tracking</h1>", unsafe_allow_html=True)
        st.write(' ')
        st.write(' ')

    with st.expander("ℹ️ - About this app", expanded=True):

        st.write(
            """     
            The *Policy Action Tracker* app is an easy-to-use interface built in Streamlit for analyzing policy documents - developed by GIZ Data and the Sustainable Development Solution Network.

            It uses a minimal keyword extraction technique that leverages multiple NLP embeddings and relies on [Transformers] (https://huggingface.co/transformers/) 🤗 to create keywords/keyphrases that are most similar to a document.
            """
        )

        st.markdown("")

    st.markdown("")
    st.markdown("##  📌 Step One: Upload document ")
    
    with st.container():

        file = st.file_uploader('Upload PDF File', type=['pdf', 'docx', 'txt'])
        
        if file is not None:
            
    
            with tempfile.NamedTemporaryFile(mode="wb") as temp:
                bytes_data = file.getvalue()
                temp.write(bytes_data)
            
                st.write("Filename: ", file.name)
                
                # load document
                docs = pre.load_document(temp.name, file)

                # preprocess document
                docs_processed, df, all_text, par_list = clean.preprocessing(docs)
                
                # testing
                # st.write(len(all_text))
                # for i in par_list:
                #     st.write(i)

                @st.cache(allow_output_mutation=True)
                def load_keyBert():
                    return KeyBERT()

                kw_model = load_keyBert()

                keywords = kw_model.extract_keywords(
                all_text,
                keyphrase_ngram_range=(1, 2),
                use_mmr=True,
                stop_words="english",
                top_n=15,
                diversity=0.7,
                )

                st.markdown("## 🎈 What is my document about?")
            
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

                ######## SDG classiciation
                # @st.cache(allow_output_mutation=True)
                # def load_sdgClassifier():
                #     classifier = pipeline("text-classification", model= "../models/osdg_sdg/")

                #     return classifier
                
                # load from disc (github repo) for performance boost
                @st.cache(allow_output_mutation=True)
                def load_sdgClassifier():
                    classifier = pipeline("text-classification", model= "../models/osdg_sdg/")

                    return classifier

                classifier = load_sdgClassifier()

                # # not needed, par list comes from pre_processing function already

                # word_list = all_text.split()
                # len_word_list = len(word_list)
                # par_list = []
                # par_len = 130
                # for i in range(0,len_word_list // par_len):
                #     string_part = ' '.join(word_list[i*par_len:(i+1)*par_len])
                #     par_list.append(string_part)
                    
                labels = classifier(par_list)
                labels_= [(l['label'],l['score']) for l in labels]
                df = DataFrame(labels_, columns=["SDG", "Relevancy"])
                df['text'] = par_list      
                df = df.sort_values(by="Relevancy", ascending=False).reset_index(drop=True)  
                df.index += 1
                df =df[df['Relevancy']>.85]
                x = df['SDG'].value_counts()

                plt.rcParams['font.size'] = 25
                colors = plt.get_cmap('Blues')(np.linspace(0.2, 0.7, len(x)))
                # plot
                fig, ax = plt.subplots()
                ax.pie(x, colors=colors, radius=2, center=(4, 4),
                    wedgeprops={"linewidth": 1, "edgecolor": "white"}, frame=False,labels =list(x.index))

                st.markdown("## 🎈 Anything related to SDGs?")

                c4, c5, c6 = st.columns([5, 7, 1])

                # Add styling
                cmGreen = sns.light_palette("green", as_cmap=True)
                cmRed = sns.light_palette("red", as_cmap=True)
                df = df.style.background_gradient(
                    cmap=cmGreen,
                    subset=[
                        "Relevancy",
                    ],
                )

                format_dictionary = {
                    "Relevancy": "{:.1%}",
                }

                df = df.format(format_dictionary)

                with c4:
                    st.pyplot(fig)
                with c5:
                    st.table(df) 
                
                

