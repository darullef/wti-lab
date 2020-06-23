import redis
import pandas as pd
import numpy as np
import json

redis_1 = redis.Redis(host='localhost', port=6379, db=1)
redis_2 = redis.Redis(host='localhost', port=6379, db=2)

df = pd.read_csv('../data/user_ratedmovies.dat', nrows=10000, delimiter="\t",
                 usecols=["userID", "movieID", "rating"])
df1 = pd.read_csv('../data/movie_genres.dat', delimiter="\t",
                  usecols=["movieID", "genre"])


def pivot_movie_all_genres():
    all_genres = []
    pd.set_option('expand_frame_repr', False)
    df1["value"] = 1
    df2 = df1.pivot_table(index="movieID", columns="genre", values="value", fill_value=np.nan)
    for genre in df2.columns:
        all_genres.append(genre)
        df2.rename(columns={genre: genre}, inplace=True)
    merged_table = pd.merge(df, df2, on='movieID')
    return merged_table, all_genres


def pivot_movie_genre():
    data_frame_1 = pd.read_csv('../data/user_ratedmovies.dat', nrows=10000, delimiter="\t",
                               usecols=["userID", "movieID", "rating"])

    data_frame_2 = pd.read_csv('../data/movie_genres.dat', delimiter="\t",
                               usecols=["movieID", "genre"])
    return pd.merge(data_frame_1, data_frame_2, on='movieID', how='inner')


def to_json(data_frame):
    return data_frame.to_json(orient='records')


def to_dict(data_frame):
    return data_frame.to_dict(orient='records')
