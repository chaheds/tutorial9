import streamlit as st
import time

st.balloons()
st.subheader('progress bar')
st.progress(10)

st.subheader('wait for the execution')
with st.spinner('wait for it...'):
    time.sleep(10)
    