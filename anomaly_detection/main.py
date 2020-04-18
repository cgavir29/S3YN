from log_parser import LogParser

# lp1 = LogParser('HDFS_1K.log')
lp1 = LogParser('HDFS_10.log')
lp1.anonymize()
print(lp1.anonymized_data)
lp1.tokenize()
print(lp1.bins)