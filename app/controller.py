import random
import sys
import time
from app import CONFIG
from mongoengine import *
from .feed import *
from Adafruit_IO import MQTTClient

ADAFRUIT_IO_KEY = CONFIG['AIO_KEY']
ADAFRUIT_IO_USERNAME = CONFIG['AIO_USERNAME']

register_connection (
	alias = "default",
	name = CONFIG["DB_NAME"],
	username = CONFIG["DB_USERNAME"],
	password = CONFIG["DB_PASSWORD"],
	host = CONFIG["DB_HOST"],
	port = CONFIG["DB_PORT"]
)

def connected(client):
	print('Connected to Adafruit IO!  Listening for DemoFeed changes...')
	client.subscribe('digital')

def disconnected(client):
    print('Disconnected from Adafruit IO!')
    sys.exit(1)

def message(client, feed_id, payload, retain):
    print('Feed {0} received new value: {1}'.format(feed_id, payload))
    g = Gauge('Gauge', feed_id, payload)
    g.save()
    Gauge.objects().update_one(upsert=True)


def load_client():
	client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

	client.on_connect    = connected
	client.on_disconnect = disconnected
	client.on_message    = message

	client.connect()
	client.loop_background()