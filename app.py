import streamlit as st
import pickle
import pandas as pd
import requests

# Load movie data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Function to get movie poster
def get_poster(movie_id):
    url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8'
    try:
        data = requests.get(url, timeout=5).json()
        poster_path = data.get('poster_path')
        if poster_path:
            return f"https://image.tmdb.org/t/p/w500/{poster_path}"
    except:
        pass
    return "https://via.placeholder.com/500x750?text=No+Poster"

# Function to recommend movies
def recommend(movie):
    # Find movie position
    index = movies[movies['title'] == movie].index[0]
    
    # Get similarity scores
    distances = list(enumerate(similarity[index]))
    
    # Sort by similarity and get top 5
    sorted_movies = sorted(distances, reverse=True, key=lambda x: x[1])[1:6]
    
    # Get movie names and posters
    recommended_movies = []
    recommended_posters = []
    
    for i in sorted_movies:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(get_poster(movie_id))
    
    return recommended_movies, recommended_posters

# Title
st.title('🎬 Movie Recommender System')
st.write('Find movies similar to your favorite!')

# Select movie
selected_movie = st.selectbox('Choose a movie:', movies['title'].values)

# Recommend button
if st.button('Show Recommendations'):
    names, posters = recommend(selected_movie)
    
    # Show 5 movies in columns
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.text(names[0])
        st.image(posters[0])
    
    with col2:
        st.text(names[1])
        st.image(posters[1])
    
    with col3:
        st.text(names[2])
        st.image(posters[2])
    
    with col4:
        st.text(names[3])
        st.image(posters[3])
    
    with col5:
        st.text(names[4])
        st.image(posters[4])
