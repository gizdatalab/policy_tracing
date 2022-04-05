import streamlit as st

def app():
    # Sidebar
    st.sidebar.title('Analyse Policy Document')

    # Container
    with st.container():
        st.markdown("<h1 style='text-align: center; color: black;'>SDSN X GIZ Policy Tracing</h1>",
                    unsafe_allow_html=True)
        file = st.file_uploader('Upload', type=['pdf'])

        if file is not None:
            st.write('... ')
        else:
            st.write(' ')
            st.write(' ')
            st.markdown("<h1 style='text-align: center; color: black;'>no PDF uploaded ...</h1>",
                        unsafe_allow_html=True)
