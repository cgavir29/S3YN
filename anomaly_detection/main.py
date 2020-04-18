from log_parser import LogParser

# lp1 = LogParser('HDFS_10.log')
lp1 = LogParser('HDFS_100.log')
# lp1 = LogParser('HDFS_1K.log')
events, blk_events = lp1.parse()

print(f'Total Events {len(events)}:')
print(events)
print()
# print('Blk-Events:')
# print(blk_events)

print(lp1.bins)
