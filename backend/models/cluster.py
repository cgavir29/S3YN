from mongoengine import EmbeddedDocument, StringField, IntField, ListField, DictField


class Cluster(EmbeddedDocument):
    # centroid = ListField(required=True)
    # status = StringField(max_length=30, required=True)  # Normal/Anomaly
    possible_abnormal_events = IntField(required=True)
    outliers = DictField()
