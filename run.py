import random
import sys
import time
import config as CONFIG
from mongoengine import *
from feed import *
from Adafruit_IO import MQTTClient

AIO_KEY = CONFIG.KEY
AIO_USERNAME = CONFIG.USERNAME

register_connection (
	alias = "default",
	name = CONFIG.DB_NAME,
	username = CONFIG.DB_USERNAME,
	password = CONFIG.DB_PASSWORD,
	host = CONFIG.DB_HOST,
	port = CONFIG.DB_PORT
)

def connected(client):
	print('Connected to AIO & listening for digital feed changes')
	client.subscribe('digital')

def disconnected(client):
	print('Disconnected from AIO')
	sys.exit(1)

def message(client, feed_id, payload):
	print('Feed {0} received value {1}'.format(feed_id, payload))
	g = Gauge('Gauge', feed_id, payload)
	g.save()
	Gauge.objects().update_one(upsert=True)

client = MQTTClient(AIO_USERNAME, AIO_KEY)

client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message

client.connect()
client.loop_blocking()