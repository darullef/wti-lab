import que
import json
import time


def consumer_2(name):
    redis = que.Que()
    print(redis.rpop(name))
    if not redis.exists(name):
        print('wrong key')
    else:
        records = redis.get_all(name)
        end = time.time() + 10
        while time.time() < end:
            for x in records:
                if x is None:
                    print('no data to display')
                else:
                    print(json.loads(x.decode('utf-8')))
                time.sleep(1.00 / 4)
