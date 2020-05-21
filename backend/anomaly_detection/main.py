from log_parser import LogParser
from feature_extractor import FeatureExtractor
from clustering import Clustering
from idf import IDF

parser = LogParser('../../data/HDFS_2K.log')
tagged_events, log_sequences = parser.parse()

extractor = FeatureExtractor(log_sequences, list(tagged_events.keys()))
log_sequences = extractor.extract()

clustering = Clustering(log_sequences, tagged_events)
cluster_ids, cluster_values = clustering.cluster()

"""
for cluster_value in cluster_values:
    if cluster_value['num_possible_abnormal_events'] != 0:
        print(cluster_value)
        print()
"""
#print ("El coeficiente de silueta es =", silhouette)

