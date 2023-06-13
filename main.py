
import streamlit as st
import pandas as pd



st.set_page_config(layout="wide", page_title="Movie Portfolio", page_icon="")

st.header("Movies Portfolio")
st.image("images/ramayan.png")
st.subheader("This portfolio gives information about Anime movie")

col1,col2 = st.columns(2)
df = pd.read_csv("movie_data.csv", sep=";")

with col1:
    for index, row in df[:3].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("Images/" + row["image"])


with col2:
    for index, row in df[3:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("Images/" + row["image"])


