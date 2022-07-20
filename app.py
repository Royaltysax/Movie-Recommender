import pandas as pd
import pickle
import streamlit as st

def recommend_movies(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    similar_movies = list(enumerate(similarity[movie_index]))
    sorted_similar_movies = sorted(similar_movies, key=lambda x:x[1], reverse=True)[1:11]

    recommended_movies = []

    for x in sorted_similar_movies:
        recommended_movies.append(movies.iloc[x[0]].title)
    
    return recommended_movies


movies_dict = pickle.load(open('recommender.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.header('MOVIE RECOMMENDER SYSTEM')

selected_movie = st.selectbox('Selet Movie: ', movies['title'].values)

if st.button('Recommend Movies'):
    names = recommend_movies(selected_movie)

    st.text(f"Top 10 Movie Recommendations along '{selected_movie}'")

    for i in range(0, 10):
        st.text(f'{i+1}. {names[i]}')
   