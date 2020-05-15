from mongoengine import EmbeddedDocument, StringField


STATUS_CHOICES = [
    'Normal',
    'Anomaly'
]


class Event(EmbeddedDocument):
    name = StringField(required=True)  # Pepito * juanito
    status = StringField(choices=STATUS_CHOICES, required=True)
