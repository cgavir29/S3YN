import numpy as np # para realizar calculos avanzados
import pandas as pd # para el analisis de datos

import scipy.cluster.hierarchy as sch
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

from pymongo import MongoClient

class Clustering():
    def __init__(self, log_sequences, events, possible_abnormal_events):
        self.log_sequences = log_sequences
        self.events = events
        self.possible_abnormal_events = possible_abnormal_events

        self.clusters = {}
        self.possible_abnormal_clusters = []

        self.client = MongoClient('mongodb+srv://s3yn:s3yn@pi2-j348a.mongodb.net/test?retryWrites=true&w=majority')
        self.db = self.client.test

    def cluster(self):
        self.generate_clusters()
        self.calculate_centroid()
        self.generate_possible_abnormal_clusters()

        '''collection = self.db['cluster']
        cursor = collection.find({})

        for document in cursor:
          print(str(document['centroid']) + ' -> ' + str(document['status']))
        '''
        return self.log_sequences, self.clusters

    def generate_clusters(self):
        log_sequence_ids = list(self.log_sequences.keys())
        features_vectors = [log_sequence_value['Features Vector']  for log_sequence_value in list(self.log_sequences.values())]

        hierarchy_clustering = linkage(features_vectors, 'ward')
        cluster_ids = fcluster(hierarchy_clustering, t=2, criterion ='distance')

        i = 0
        for cluster_id in cluster_ids:    
            if cluster_id in self.clusters: self.clusters[cluster_id]['Log Sequence IDs'].append(log_sequence_ids[i])
            else: self.clusters[cluster_id] = {'Log Sequence IDs': [log_sequence_ids[i]]}
            i += 1

    def calculate_centroid(self):
        for cluster_id in self.clusters:
            features = [self.log_sequences[log_sequence_id]['Features Vector'] for log_sequence_id in self.clusters[cluster_id]['Log Sequence IDs']]
            
            arr = np.array(features)
            length, dim = arr.shape
            
            centroid = np.array([np.sum(arr[:, i])/length for i in range(dim)])
            
            self.clusters[cluster_id]['Centroid'] = centroid
            
            self.clusters[cluster_id]['Events'] = []
            
            for event_centroid_index in range(len(centroid)): 
                if centroid[event_centroid_index] != 0: self.clusters[cluster_id]['Events'].append(self.events[event_centroid_index]) 
           
    def generate_possible_abnormal_clusters(self):
        for cluster_id in self.clusters:
            centroid = self.clusters[cluster_id]['Centroid']

            num_possible_abnormal_events = 0 # Número de posibles eventos anómalos en el clúster.
            
            self.clusters[cluster_id]['Posibble Abnormal'] = {}

            for possible_abnormal_event_index in self.possible_abnormal_events:
                possible_abnormal_log_sequences = [] # En qué log_sequences está el posible evento anómalo.
                
                if centroid[possible_abnormal_event_index] != 0:
                    num_possible_abnormal_events += 1
                    
                    for log_sequence_id in self.clusters[cluster_id]['Log Sequence IDs']:
                        if self.log_sequences[log_sequence_id]['Representative Log Sequence'][possible_abnormal_event_index] == 1:
                            possible_abnormal_log_sequences.append(log_sequence_id)
                
                self.clusters[cluster_id]['Posibble Abnormal'][possible_abnormal_event_index] = possible_abnormal_log_sequences

            self.clusters[cluster_id]['Num Possible Abnormal'] = num_possible_abnormal_events

            #print('For cluster_id ' + str(cluster_id) + ' we have ' + str(num_possible_abnormal_events) + ' possible abnormal events.')