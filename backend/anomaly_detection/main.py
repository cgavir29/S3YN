from log_parser import LogParser
from feature_extractor import FeatureExtractor
from clustering import Clustering

parser = LogParser('HDFS_1K.log')
events, blk_events = parser.parse()

extractor = FeatureExtractor(events, blk_events)
log_sequences = extractor.extract()

clustering = Clustering(log_sequences)
clustering.cluster()
