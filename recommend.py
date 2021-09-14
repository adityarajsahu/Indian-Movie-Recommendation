import numpy as np
import pandas as pd
from dataprocessor import processor

movies = pd.read_csv("Dataset/Top3000_imdb_indian_movies.csv")
DataFrame = processor(movies)

print(DataFrame.shape)