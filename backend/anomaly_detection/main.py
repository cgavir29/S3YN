from log_parser import LogParser
from feature_extractor import FeatureExtractor
from clustering import Clustering
from idf import IDF

parser = LogParser('../../data/HDFS.log')
events, log_sequences = parser.parse()

for event in events:
    print(event)

#extractor = FeatureExtractor(log_sequences, events)
#log_sequences = extractor.extract()

# Se saca una lista con los posibles eventos anómalos.
abnormal = [11]

#clustering = Clustering(log_sequences, events, abnormal)
#log_sequences, clusters = clustering.cluster()

'''for cluster_id in clusters:
    print('Cluster ID: ' + str(cluster_id))
    print('Num possible abnormal: ' + str(clusters[cluster_id]['Num Possible Abnormal']))
    print(clusters[cluster_id]['Posibble Abnormal'])
    print()'''