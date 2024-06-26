from tempfile import NamedTemporaryFile
import pysrt
import streamlit as st

st.title('pysrt Test for Streamlit')

uploaded_file = st.file_uploader("Choose a .srt file", type="srt")

if uploaded_file is not None:
    with NamedTemporaryFile(suffix='.srt', delete=False) as tempfile:
        st.info(tempfile.name)
        tempfile.write(uploaded_file.getbuffer())
        sub = pysrt.open(tempfile.name, encoding='utf-8')
    texts = sub.text
    st.markdown(texts, unsafe_allow_html=True)
