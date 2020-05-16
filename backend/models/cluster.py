from mongoengine import EmbeddedDocument, StringField, IntField, ListField, DictField


class Cluster(EmbeddedDocument):
    centroid = ListField(required=True)
    possible_abnormal_events = IntField(required=True)
    outliers = DictField()
