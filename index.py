import streamlit as st
from streamlit import caching
import os
from src.core.translate import Translator_M
from src.core.utils import utils

st.title('1stDayKit Machine Translation')
st.write('1stDayKit is a high-level Deep Learning toolkit for solving generic tasks.')

Trans = Translator_M(task='Helsinki-NLP/opus-mt-en-ROMANCE')

col1, col2 = st.beta_columns(2)

sentence = col1.text_input('Type the text to translate here:')

option = col2.selectbox('Translate to',['fr','pt','es'])

if st.button('Translate'):
    st.spinner()
    with st.spinner(text='Loading...'):
        text_to_translate = ['>>{lang}<< {input}'.format(lang=option,input=sentence)]
        output = Trans.predict(text_to_translate)
        st.code(output[0])