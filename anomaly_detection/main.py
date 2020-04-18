from log_parser import LogParser
from feature_extractor import FeatureExtractor

extractor = FeatureExtractor('HDFS_1K.log')

extractor.extract()


# lp1 = LogParser('HDFS_10.log')
#lp1 = LogParser('HDFS_100.log')
# lp1 = LogParser('HDFS_1K.log')
'''lp1 = LogParser('HDFS_10.log')
lp1.anonymize()
print(lp1.anonymized_data)
lp1.tokenize()
print(lp1.bins)'''
