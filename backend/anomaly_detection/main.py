from log_parser import LogParser
from feature_extractor import FeatureExtractor
from clustering import Clustering
from idf import IDF

parser = LogParser('../../data/HDFS_1K.log')
events, log_sequences = parser.parse()

extractor = FeatureExtractor(log_sequences, events)
log_sequences = extractor.extract()

clustering = Clustering(log_sequences, events)
log_sequences, clusters = clustering.cluster()
