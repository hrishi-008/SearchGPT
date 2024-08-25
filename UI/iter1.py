import streamlit as st

st.title('My first app')

with st.sidebar:
    st.write('This is a sidebar')
    st.write('You can use it to add widgets')


st.write('This is the main content area')

col1, col2 = st.columns([0.3,0.7])

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")