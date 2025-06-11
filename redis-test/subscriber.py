import redis

r = redis.Redis(host='localhost', port=6379, db=0)

pubsub = r.pubsub()
pubsub.subscribe("input")

print("waiting on input")
for message in pubsub.listen():
    if message['type'] == 'message':
        print("input:", message['data'].decode())

