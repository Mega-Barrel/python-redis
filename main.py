""" Redis Implementation """

import redis

if __name__ == "__main__":
    # do something
    r = redis.Redis(
        host='localhost',
        port=6379
    )
    redis_cli = redis.Redis(
        host='localhost',
        port=6379,
        charset="utf-8",
        decode_responses=True
    )

    #Set your key
    redis_cli.set("United Kingdom", "London")
    redis_cli.set("Germany", "Berlin")
    redis_cli.set("India", "New Delhi")

    #Get the value of inserted key
    print(redis_cli.get('United Kingdom'))
    print(redis_cli.get('Germany'))
    print(redis_cli.get('India'))
