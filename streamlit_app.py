import streamlit as st

st.title("🎈 My new app title HERE")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.markdown("this is the markdown")
st.header("this is a header")
st.subheader("This is a subheader")
st.caption("this is a caption")
st.code("x=2024")
st.latex(r'''
         a + a r^1 + a r^2 + a r^3''')
st.checkbox("yes")
st.button('Click')
st.radio('Pick your gender', ['Male', 'Female'])
st.selectbox('Pick your gender', ['Male', 'Female'])
st.multiselect('choose a planet', ['Jupiter', 'Mars', 'Neptune'])
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])
st.slider('Pick a number', 0,50)
st.number_input('Pick a number', 0,10)
st.text_input('Email address')
st.date_input('Travelling date')
st.time_input('School time')
st.text_area('Description')
st.file_uploader('Upload a photo')
st.color_picker('Choose your favorite color')

st.sidebar.title('This is written inside the sidebar')
st.sidebar.button('Click')
st.sidebar.radio('Pick your gender', ['Male', 'Female'])
