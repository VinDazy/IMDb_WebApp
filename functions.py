from key import key

# function that returns random movies to display on the welcome page
def get_random_movies_data():
    import requests


    url = "https://moviesdatabase.p.rapidapi.com/titles/random"
    querystring = {"startYear": "2022", "endYear": "2023", "list": "most_pop_movies"}
    headers = {
        "X-RapidAPI-Key": key.api_key,
        "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = response.json()['results']
    movies_data = []

    for movie in data:
        movie_name = movie['originalTitleText']['text']
        if movie['primaryImage']['url'] is not None:
                movie_poster = movie['primaryImage']['url']
        else:
             movie_poster='media/image_not_found.jpg'
        movie_type = movie['titleType']['text']
        release_year = movie['releaseYear']['year']

        movie_dict = {
            'name': movie_name,
            'poster': movie_poster,
            'type': movie_type,
            'release year': release_year
        }

        movies_data.append(movie_dict)
    return movies_data

def display_movies():
    import streamlit as st
    col1,col2=st.columns(2)
    random_movies=get_random_movies_data()
    poster_width = 300  

    for idx, movie in enumerate(random_movies):
        with col1 if idx % 2 == 0 else col2:
            st.image(movie['poster'], caption=movie['name'], width=poster_width)
            with st.expander("More Info"):
                st.write(f"Type: {movie['type']}")
                st.write(f"Release Year: {movie['release year']}")
    
def switch_page():
     import streamlit as st
     st.write("Hello world")

