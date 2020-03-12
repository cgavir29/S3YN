from mongoengine import *

class Database(Document):
    name = StringField(max_length=100, required=True)
    url = StringField(max_length=255, required=True)
    username = StringField(max_length=100, required=True)
    password = StringField(max_length=200, required=True)
