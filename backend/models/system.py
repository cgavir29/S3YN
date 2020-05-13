from mongoengine import Document, StringField, DictField, ListField, EmbeddedDocumentListField
from .event import Event


class System(Document):
    name = StringField(unique=True, required=True)
    events = EmbeddedDocumentListField(Event, required=True)
