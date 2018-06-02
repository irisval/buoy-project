from mongoengine import *
import datetime

class Gauge(Document):
	meta = {
		"strict": False
	}
	block_type = StringField(required=True)
	feed_name = StringField(required=True)
	value = IntField(default=0, required=True)
	created_at = DateTimeField(default=datetime.datetime.now, required=True)
	# location = GeoPointField()