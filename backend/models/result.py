from mongoengine import Document, ReferenceField, StringField, EmbeddedDocumentListField
from .user import User
from .event import Event
from .cluster import Cluster


class Result(Document):
    user_id = ReferenceField(User)
    name = StringField(required=True)
    events = EmbeddedDocumentListField(Event, required=True)
    clusters = EmbeddedDocumentListField(Cluster, required=True)
