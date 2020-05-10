from mongoengine import Document, StringField, ListField


class Cluster(Document):
    centroid = ListField(required=True)
    status = StringField(max_length=30, required=True)  # Normal/Anomaly
