from mongoengine import EmbeddedDocument, StringField


class Event(EmbeddedDocument):
    name = StringField(required=True)  # Pepito * juanito
    status = StringField(required=True)
