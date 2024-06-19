import redis
import json

# Connect to the Redis server (localhost by default, port 6379)
redis_client = redis.Redis(
    host='localhost',
    port=6379,
    db=0,
    password='password'
)


def store_session_data(session_id, data):
    redis_client.set(session_id, json.dumps(data))


def get_session_data(session_id):
    data = redis_client.get(session_id)
    if data is not None:
        return json.loads(data)
    else:
        return None


# Example usage
session_id = 'abc123'
data = {'name': 'Alice', 'age': 25}
store_session_data(session_id, data)
print(get_session_data(session_id))  # Output: {'name': 'Alice', 'age': 25}

redis_client.expire(session_id, session_timeout_seconds)  # Set expiration time in seconds
print(redis_client.ttl(session_id))  # Output: Remaining time in seconds