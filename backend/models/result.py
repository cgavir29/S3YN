from mongoengine import *

class Result(Document): 
    # user_id = 
    name = StringField(max_length=20, required=True)
    log = StringField(max_length=20, required=True)
