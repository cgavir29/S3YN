import csv

# Generate file with first 1000 lines of the HDFS dataset
with open('HDFS.log', 'r') as hdfs:
    with open('HDFS_1K.log', 'w') as hdfs_1k:
        for _ in range(1000):
            hdfs_1k.write(hdfs.readline())

# Generate file with first 1000 lines of the anomaly_label dataset
# with open('anomaly_label.csv', 'r') as anomaly_label:
#     al_reader = csv.reader(anomaly_label)

#     with open('anomaly_label_1k.csv', 'w') as anomaly_label_1k:
#         al_1k_writer = csv.writer(anomaly_label_1k)

#         i = 0
#         for row in al_reader:
#             if i == 11:
#                 break

#             print(row)
#             i += 1
#             al_1k_writer.writerow([value for value in row])
