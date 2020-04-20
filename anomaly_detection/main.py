from log_parser import LogParser
from feature_extractor import FeatureExtractor

parser = LogParser('HDFS_100.log')
events, blk_events = parser.parse()

extractor = FeatureExtractor(events, blk_events)
extractor.extract()
