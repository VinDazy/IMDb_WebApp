# function that returns random movies to display on the welcome page
def get_random_movies_data():
    import requests


    url = "https://moviesdatabase.p.rapidapi.com/titles/random"
    querystring = {"startYear": "2022", "endYear": "2023", "list": "most_pop_movies"}
    headers = {
        "X-RapidAPI-Key": "62b620fdabmsh9245da47d990846p1f3c48jsn3e6be629f08b",
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
    

