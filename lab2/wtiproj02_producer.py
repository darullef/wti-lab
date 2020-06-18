import que
from lab2 import fake_json
import json
import time
import pandas as p


def producer_1(name):
    i = 0
    q = que.Que()
    while i < 1000:
        fjson = fake_json.fakeJson()
        js = json.dumps(fjson)
        q.lpush(name, js)
        i += 1
        time.sleep(0.01)


def producer_2(name):
    redis = que.Que()
    df = p.read_csv('../data/user_ratedmovies.dat', sep=" ", header=None, nrows=100,
                    delimiter="\t",
                    names=['userID', 'movieID', 'rating',
                           'date_day', 'date_month', 'date_year',
                           'date_hour', 'date_minute', 'date_second'])
    for index, row in df.iterrows():
        print(row)
        js = json.dumps(row.to_dict())
        redis.lpush(name, js)
        time.sleep(1.00 / 4)
