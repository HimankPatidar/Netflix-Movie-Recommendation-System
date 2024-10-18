import pickle
import pandas as pd
import streamlit as st

# Load the movie metadata and similarity matrix
movies_metadata = pickle.load(open('./movie_dict.pkl', mode='rb'))
movies = pd.DataFrame(movies_metadata)
similarity = pickle.load(open('similarity.pkl', mode='rb'))

# Function to recommend a movie
def recommend(movie):
    recommend = []
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]

    for i in movie_list:
        recommend.append(movies.iloc[i[0]]['title'])  

    return recommend

# STREAMLIT Web-App
st.title('Movie Recommendation System')
selected_movie = st.selectbox("Select a movie to get some recommendations :", movies['title'].values)  
btn = st.button('Recommend')

if btn:
    recommended_movies = recommend(selected_movie)

    for i in recommended_movies:
        st.write(i)
