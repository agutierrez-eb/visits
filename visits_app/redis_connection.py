from redis import Redis


class RedisConnection:

    def __init__(self):
        self.client = Redis(host='redis-server', port=6379, db=0)
        self.client.set('visits', '0')

    def get_visits(self):
        return self.client.get('visits')

    def increment_visits(self):
        my_visits = int(self.client.get('visits'))
        self.client.set('visits', my_visits + 1)
