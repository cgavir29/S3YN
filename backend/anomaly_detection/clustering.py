import numpy as np # para realizar calculos avanzados
import pandas as pd # para el analisis de datos

import scipy.cluster.hierarchy as sch
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

class Clustering():
    def __init__(self, log_sequences):
        self.log_sequences = log_sequences
        self.clusters = {}
       
    def cluster(self):
        self.generate_clusters()
        self.calculate_centroid()

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
            # Features vectors of the cluster
            features = [self.log_sequences[log_sequence_id]['Features Vector'] for log_sequence_id in self.clusters[cluster_id]['Log Sequence IDs']]
            
            arr = np.array(features)
            length, dim = arr.shape
            
            centroid = np.array([np.sum(arr[:, i])/length for i in range(dim)])
            
            self.clusters[cluster_id]['Centroid'] = centroid
           