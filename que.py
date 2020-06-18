import redis


class Que:

    def __init__(self):
        self.r = redis.Redis(host='localhost', port=6379, db=0)

    def exists(self, name):
        return self.r.exists(name)

    def lpush(self, name, value):
        self.r.lpush(name, value)

    def rpop(self, name):
        self.r.rpop(name)

    def llen(self, name):
        self.r.llen(name)

    def print(self, name):
        for x in self.r.lrange(name, 0, -1):
            print(x)

    def fifo(self, name):
        for x in self.r.lrange(name, 0, -1):
            return self.rpop(name)

    def get_all(self, name):
        return self.r.lrange(name, 0, -1)

    def flush(self, name):
        self.r.flushdb()

