""" Redis Implementation """

import redis

if __name__ == "__main__":
    # do something
    r = redis.Redis(
        host='localhost',
        port=6379
    )
    r.set("United Kingdom", "London")
    r.set("Germany", "Berlin")
    r.set("India", "New Delhi")
