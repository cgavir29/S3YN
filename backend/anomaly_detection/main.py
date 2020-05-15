from log_parser import LogParser
from feature_extractor import FeatureExtractor
from clustering import Clustering
from idf import IDF

parser = LogParser('../../data/HDFS_2K.log')
tagged_events, log_sequences = parser.parse()

extractor = FeatureExtractor(log_sequences, list(tagged_events.keys()))
log_sequences = extractor.extract()

events = list(tagged_events.keys())
possible_abnormal_events = []

for key, value in tagged_events.items():
    if value == 'WARN': possible_abnormal_events.append(key)

print(possible_abnormal_events)

clustering = Clustering(log_sequences, events, possible_abnormal_events)
log_sequences, clusters = clustering.cluster()

for cluster_value in list(clusters.values()):
    if cluster_value['possible_abnormal_events'] != 0:
        print(cluster_value)
        print()