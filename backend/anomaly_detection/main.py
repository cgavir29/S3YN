from log_parser import LogParser
from feature_extractor import FeatureExtractor
from clustering import Clustering

parser = LogParser('HDFS_1K.log')
events, log_sequences = parser.parse()

print(log_sequences[list(log_sequences.keys())[27]])

extractor = FeatureExtractor(log_sequences, events)
log_sequences = extractor.extract()

print(log_sequences[list(log_sequences.keys())[27]])

clustering = Clustering(log_sequences)
log_sequences, clusters = clustering.cluster()

print(log_sequences[list(log_sequences.keys())[27]])
print(len(clusters))