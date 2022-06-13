import pandas as pd
import numpy as np
import string  
import nltk 
import spacy
import en_core_web_sm
import re
import streamlit as st

from haystack.nodes import PreProcessor

'''basic cleaning - suitable for transformer models'''
def basic(s):
    """
    :param s: string to be processed
    :return: processed string: see comments in the source code for more info
    """
    # Text Lowercase
    s = s.lower() 
    # Remove punctuation
    translator = str.maketrans(' ', ' ', string.punctuation) 
    s = s.translate(translator)
    # Remove URLs
    s = re.sub(r'^https?:\/\/.*[\r\n]*', ' ', s, flags=re.MULTILINE)
    s = re.sub(r"http\S+", " ", s)
    # Remove new line characters
    s = re.sub('\n', ' ', s) 
  
    # Remove distracting single quotes
    s = re.sub("\'", " ", s) 
    # Remove all remaining numbers and non alphanumeric characters
    s = re.sub(r'\d+', ' ', s) 
    s = re.sub(r'\W+', ' ', s)

    # define custom words to replace:
    #s = re.sub(r'strengthenedstakeholder', 'strengthened stakeholder', s)
    
    return s.strip()


def preprocessing(document):

    """
    takes in haystack document object and splits it into paragraphs and applies simple cleaning.

    Returns cleaned list of haystack document objects. One paragraph per object. Also returns pandas df and 
    list that contains all text joined together.
    """    

    preprocessor = PreProcessor(
        clean_empty_lines=True,
        clean_whitespace=True,
        clean_header_footer=True,
        split_by="word",
        split_length=120,
        split_respect_sentence_boundary=True,
        #split_overlap=5
    )
    for i in document:
        docs_processed = preprocessor.process([i])
        for item in docs_processed:
            item.content = basic(item.content)

    st.write("your document has been splitted to", len(docs_processed), "paragraphs")
    
    # create dataframe of text and list of all text
    df = pd.DataFrame(docs_processed)
    all_text = "".join(df.content.to_list())

    return docs_processed, df, all_text

'''processing with spacy - suitable for models such as tf-idf, word2vec'''
def spacy_clean(alpha:str, use_nlp:bool = True) -> str:

    """

    Clean and tokenise a string using Spacy. Keeps only alphabetic characters, removes stopwords and

    filters out all but proper nouns, nounts, verbs and adjectives.

    Parameters
    ----------
    alpha : str

            The input string.

    use_nlp : bool, default False

            Indicates whether Spacy needs to use NLP. Enable this when using this function on its own.

            Should be set to False if used inside nlp.pipeline   

     Returns
    -------
    ' '.join(beta) : a concatenated list of lemmatised tokens, i.e. a processed string

    Notes
    -----
    Fails if alpha is an NA value. Performance decreases as len(alpha) gets large.
    Use together with nlp.pipeline for batch processing.

    """

    nlp = spacy.load("en_core_web_sm", disable=["parser", "ner", "textcat"])

    if use_nlp:

        alpha = nlp(alpha)

        

    beta = []

    for tok in alpha:

        if all([tok.is_alpha, not tok.is_stop, tok.pos_ in ['PROPN', 'NOUN', 'VERB', 'ADJ']]):

            beta.append(tok.lemma_)

            
    text = ' '.join(beta)
    text = text.lower()
    return text