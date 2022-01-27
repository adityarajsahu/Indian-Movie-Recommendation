import pandas as pd
import streamlit as st
import pickle


def recommend(movie):
    index = movie_df[movie_df['Title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movies = []
    imdb_ratings = []
    for i in distances[1:6]:
        recommended_movies.append(movie_df.iloc[i[0]].Title)
        imdb_ratings.append(movie_df.iloc[i[0]].ImDBRating)

    new_df = pd.DataFrame({'Recommended Movies': recommended_movies, 'IMDB Rating': imdb_ratings})
    return new_df


st.header('Indian Movie Recommendation System')

movie_df = pickle.load(open('SavedModel/movies.pkl', 'rb'))
similarity = pickle.load(open('SavedModel/similarity.pkl', 'rb'))

all_movie_names = movie_df['Title'].values
input_movie = st.selectbox('Enter the movie name or select from the dropdown', all_movie_names)

if st.button('Recommend'):
    output_df = recommend(input_movie)
    st.table(output_df)
