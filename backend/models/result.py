from mongoengine import Document, StringField, DictField, ReferenceField, ListField
from .user import User

class Result(Document):
    user_id = ReferenceField(User)
    name = StringField(max_length=30, required=True)
    log = StringField(max_length=30, required=True)
    events = ListField(required=True)
    features = DictField(required=True)
    anomalies = DictField(required=True)
