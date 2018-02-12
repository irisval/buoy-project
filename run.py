import random
import sys
import time
import config as CONFIG

from Adafruit_IO import MQTTClient

AIO_KEY = CONFIG.KEY
AIO_USERNAME = CONFIG.USERNAME

def connected(client):
	print('Connected to AIO & listening for digital feed changes')
	client.subscribe('digital')

def disconnected(client):
	print('Disconnected from AIO')
	sys.exit(1)

def message(client, feed_id, payload):
	print('Feed {0} received value {1}'.format(feed_id, payload))

client = MQTTClient(AIO_USERNAME, AIO_KEY)

client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message

client.connect()
client.loop_blocking()
