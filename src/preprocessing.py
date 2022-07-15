from typing import Callable, Dict, List, Optional

from pathlib import Path
import re
import logging
import string 
import streamlit as st
logger = logging.getLogger(__name__)

import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

from haystack.utils import convert_files_to_docs, fetch_archive_from_http
from haystack.nodes.file_converter import BaseConverter, DocxToTextConverter, PDFToTextConverter, TextConverter
from haystack.schema import Document
import pdfplumber

import pandas as pd

import tempfile
import sqlite3



def load_document(
    file: str,
    file_name,
    encoding: Optional[str] = None,
    id_hash_keys: Optional[List[str]] = None,
) -> List[Document]:
    
    """
    takes docx, txt and pdf files as input and extracts text as well as the filename as metadata. Since haystack
    does not take care of all pdf files, pdfplumber is attached to the pipeline in case the pdf extraction fails
    via Haystack.

    Returns a list of type haystack.schema.Document
    """

    if file_name.name.endswith('.pdf'):
        converter = PDFToTextConverter(remove_numeric_tables=True)
    if file_name.name.endswith('.txt'):
        converter = TextConverter()
    if file_name.name.endswith('.docx'):
        converter = DocxToTextConverter()


    documents = []
    logger.info("Converting {}".format(file_name))
    # PDFToTextConverter, TextConverter, and DocxToTextConverter return a list containing a single Document
    document = converter.convert(
                file_path=file, meta=None, encoding=encoding, id_hash_keys=id_hash_keys
            )[0]
    text = document.content
    documents.append(Document(content=text, meta={"name": file_name}, id_hash_keys=id_hash_keys))
    
    '''check if text is empty and apply different pdf processor. This can happen whith certain pdf types.'''
    for i in documents: 
        if i.content == "":
            st.write("using pdfplumber")
            text = []
            with pdfplumber.open(file) as pdf:
                for page in pdf.pages:
                    text.append(page.extract_text())
            i.content = ' '.join([page for page in text])
    
    return documents

