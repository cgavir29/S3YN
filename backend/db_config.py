from mongoengine import *
from mongoengine import connect

DB_URI = 'mongodb+srv://s3yn:s3yn@pi2-j348a.mongodb.net/test?retryWrites=true&w=majority'

connect(host=DB_URI)


class Database(Document):
    name = StringField(max_length=100, required=True)
    url = StringField(max_length=255, required=True)
    username = StringField(max_length=100, required=True)
    password = StringField(max_length=200, required=True)


tr = Database(name='name', url='url', username='username', password='password')
tr.save()
