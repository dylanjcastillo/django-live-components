import redis
import json
import random
import time

REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_CHANNEL = "notifications_channel"

r = redis.StrictRedis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)


def create_random_notification():
    """Create a random notification message"""
    return {
        "id": random.randint(1, 1000),
        "title": "Notification " + str(random.randint(1, 100)),
        "message": "This is a random message " + str(random.randint(1, 100)),
        "color": random.choice(["#edafb8", "#f7e1d7", "#f9dcc4", "#b0c4b1"]),
        "timestamp": time.ctime(),
    }


def publish_notification():
    """Publish a random notification to the Redis channel"""
    notification = create_random_notification()
    r.publish(REDIS_CHANNEL, json.dumps(notification))
    print(f"Published: {notification}")


if __name__ == "__main__":
    try:
        while True:
            publish_notification()
            time.sleep(3)
    except KeyboardInterrupt:
        print("Stopped notification publisher")
