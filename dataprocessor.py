import pandas as pd
import re


def processor(df):
    df.dropna(inplace=True)
    df.drop_duplicates()
    df.drop(['Date_of_Release', 'Age_of_content', 'Votes'], axis=1, inplace=True)
    df['Genre'] = df['Genre'].apply(lambda x: re.sub(r'[^\w\s]', '', x))
    df['Crew_dir'] = df['Crew_dir'].apply(lambda x: re.sub(r'[^\w\s]', '', x))
    df['Cast_stars'] = df['Cast_stars'].apply(lambda x: re.sub(r'[^\w\s]', '', x))
    df['Plot_summary'] = df['Plot_summary'].apply(lambda x: re.sub(r'[^\w\s]', '', x))
    df['text_data'] = df[['Genre', 'Crew_dir', 'Cast_stars', 'Plot_summary']].agg(' '.join, axis=1)
    df['text_data'] = df['text_data'].apply(lambda x : " ".join(x.split()))
    df['text_data'] = df['text_data'].apply(lambda x : x.lower())
    return df