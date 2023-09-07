import streamlit as st
from functions import *
st.set_page_config(page_title="IMDb Web APP ",layout="wide", page_icon="media/imdb_icon.png")
st.title("Welcome")

sidebar=st.sidebar
with sidebar:
    sidebar.write("Welcome Kally ")

col1,col2=st.columns(2)
random_movies=get_random_movies_data()
poster_width = 300  #

for idx, movie in enumerate(random_movies):
    with col1 if idx % 2 == 0 else col2:
        st.image(movie['poster'], caption=movie['name'], width=poster_width)
        with st.expander("More Info"):
            st.write(f"Type: {movie['type']}")
            st.write(f"Release Year: {movie['release year']}")