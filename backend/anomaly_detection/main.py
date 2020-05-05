from log_parser import LogParser
from feature_extractor import FeatureExtractor
from clustering import Clustering
from idf import IDF

parser = LogParser('HDFS_1K.log')
events, blk_events = parser.parse()

extractor = FeatureExtractor(events, blk_events)
log_sequences = extractor.extract()

clustering = Clustering(log_sequences)
clustering.cluster()

calculateIDF = IDF(log_sequences)
idf = calculateIDF.getIDF()

# for x in idf:
 #    print("{0:.2f}".format(x))
