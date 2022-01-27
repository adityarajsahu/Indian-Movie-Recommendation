import numpy as np
import pandas as pd
from dataprocessor import processor
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

movies = pd.read_csv("Dataset/Top3000_imdb_indian_movies.csv")
DataFrame = processor(movies)

vec = CountVectorizer(stop_words='english', max_features=1000, max_df=0.7)
vectorized_mat = vec.fit_transform(DataFrame['text_data']).toarray()

sim = cosine_similarity(vectorized_mat)


def recommend_movies(movie):
    index = DataFrame[DataFrame['Title'] == movie].index[0]
    distances = sorted(list(enumerate(sim[index])), reverse=True, key=lambda x: x[1])
    for i in distances[1:6]:
        print(DataFrame.iloc[i[0]].Title)


recommend_movies('Shershaah')
#print(DataFrame.columns)

pickle.dump(DataFrame, open('SavedModel/movies.pkl', 'wb'))
pickle.dump(sim, open('SavedModel/similarity.pkl', 'wb'))
