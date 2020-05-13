from mongoengine import EmbeddedDocument, StringField


class Event(EmbeddedDocument):
    event = StringField(required=True)
    status = StringField(choices=('Normal', 'Anomaly'), required=True)
