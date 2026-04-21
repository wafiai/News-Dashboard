import streamlit as st 
from fetch import newsAPI,cleanoutput,Prediction

st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://images.unsplash.com/photo-1771797628441-20bc5804f48d?q=80&w=1171&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    </style>
    """,
    unsafe_allow_html=True
)
left,mid,right = st.columns([1,2,1])
st.set_page_config(layout="wide")


def fetch():
    clean = cleanoutput()
    predic = Prediction()
    with mid:
        with st.container(border=True):
            st.columns([1,4])
            newsAPI()
            st.header(clean["Title"])
            st.write(clean["Description"])
            st.button(predic)
            
                




with mid:
    st.header("Welcome to news!")
    if st.button("Click for news!"):
        fetch()
        






    