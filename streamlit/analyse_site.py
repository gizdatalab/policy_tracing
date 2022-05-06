import streamlit as st
from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import PDFPageAggregator
from pdfminer3.converter import TextConverter
import io

resource_manager = PDFResourceManager()
fake_file_handle = io.StringIO()
converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
page_interpreter = PDFPageInterpreter(resource_manager, converter)

def app():
    # Sidebar
    st.sidebar.title('Analyse Policy Document')

    # Container
    with st.container():
        st.markdown("<h1 style='text-align: center; color: black;'>SDSN X GIZ Policy Tracing</h1>",
                    unsafe_allow_html=True)
        file = st.file_uploader('Upload', type=['pdf'])
        

        with open(file, 'rb') as fh:

            for page in PDFPage.get_pages(fh,
                                          caching=True,
                                          check_extractable=True):
                page_interpreter.process_page(page)

            text = fake_file_handle.getvalue()

        # close open handles
        converter.close()
        fake_file_handle.close()


        if file is not None:
            st.write('... ')
            st.write(text)
        else:
            st.write(' ')
            st.write(' ')
            st.markdown("<h1 style='text-align: center; color: black;'>no PDF uploaded ...</h1>",
                        unsafe_allow_html=True)
