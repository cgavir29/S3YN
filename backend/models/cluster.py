from mongoengine import Document, StringField, ListField


class Cluster(Document):
    centroid = ListField()
    status = StringField(max_length=30, required=True)  # Normal/Anomaly
