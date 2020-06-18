import que
import json
import time


def consumer_1(name):
    redis = que.Que()
    if not redis.exists(name):
        print('wrong key')
    else:
        records = redis.get_all(name)
        for x in records:
            print(json.loads(x.decode('utf-8')))
            time.sleep(1.00)
