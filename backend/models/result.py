from mongoengine import Document, ReferenceField, StringField, EmbeddedDocumentListField
from .user import User
from .event import Event
from .cluster import Cluster


class Result(Document):
    user_id = ReferenceField(User)
    # name = StringField(max_length=30, required=True)
    log = StringField(max_length=30, required=True)
    events = EmbeddedDocumentListField(Event, required=True)
    # events = DictField(required=True)
    # features = DictField(required=True)
    # anomalies = DictField(required=True)
    clusters = EmbeddedDocumentListField(Cluster, required=True)
