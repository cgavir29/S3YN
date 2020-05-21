import numpy as np  # para realizar calculos avanzados
import pandas as pd  # para el analisis de datos

import scipy.cluster.hierarchy as sch
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

#from sklearn.metrics import silhouette_score
#from sklearn import model_selection

from pymongo import MongoClient


class Clustering():
    def __init__(self, log_sequences, tagged_events):
        self.log_sequences = log_sequences
        self.tagged_events = tagged_events

        self.events = []
        self.possible_abnormal_events = []

        self.clusters = {}
        self.possible_abnormal_clusters = []

        #self.silhouette = 0
        #self.crossValidation = 0

        self.client = MongoClient(
            'mongodb+srv://s3yn:s3yn@pi2-j348a.mongodb.net/test?retryWrites=true&w=majority')
        self.db = self.client.test

    def cluster(self):
        self.extract_events()
        self.generate_clusters()
        self.calculate_centroid()
        self.generate_possible_abnormal_clusters()

        '''collection = self.db['cluster']
        cursor = collection.find({})

        for document in cursor:
          print(str(document['centroid']) + ' -> ' + str(document['status']))
        '''

        return list(self.clusters.keys()), list(self.clusters.values())
        #self.silhouette, self.crossValidation

    def extract_events(self):
        self.events = list(self.tagged_events.keys())

        for key, value in self.tagged_events.items():
            if value == 'WARN':
                self.possible_abnormal_events.append(key)

    def generate_clusters(self):
        log_sequence_ids = list(self.log_sequences.keys())
        features_vectors = [log_sequence_value['Features Vector']
                            for log_sequence_value in list(self.log_sequences.values())]

        hierarchy_clustering = linkage(features_vectors, 'ward')
        cluster_ids = fcluster(hierarchy_clustering, t=2, criterion='distance')

        #self.silhouette = silhouette_score(features_vectors, cluster_ids, metric='euclidean')

        #scoring = {'acc': 'accuracy',
        #           'prec_macro': 'precision_macro',
        #           'rec_micro': 'recall_macro'}
        #scores = model_selection.cross_validate(cluster_ids, features_vectors.data, features_vectors.target, scoring=scoring, cv=5, return_train_score=True)

        i = 0
        for cluster_id in cluster_ids:
            if cluster_id in self.clusters:
                self.clusters[cluster_id]['Log Sequence IDs'].append(
                    log_sequence_ids[i])
            else:
                self.clusters[cluster_id] = {
                    'Log Sequence IDs': [log_sequence_ids[i]]}
            i += 1

    def calculate_centroid(self):
        for cluster_id in self.clusters:
            features_vectors_cluster = [self.log_sequences[log_sequence_id]['Features Vector']
                                        for log_sequence_id in self.clusters[cluster_id]['Log Sequence IDs']]

            arr = np.array(features_vectors_cluster)
            length, dim = arr.shape

            centroid = np.array([np.sum(arr[:, i])/length for i in range(dim)])

            self.clusters[cluster_id]['centroid'] = centroid
            self.clusters[cluster_id]['Events'] = []

            for event_centroid_index in range(len(centroid)):
                if centroid[event_centroid_index] != 0:
                    self.clusters[cluster_id]['Events'].append(
                        self.events[event_centroid_index])

    def generate_possible_abnormal_clusters(self):
        for cluster_id in self.clusters:
            centroid = self.clusters[cluster_id]['centroid']

            self.clusters[cluster_id]['num_possible_abnormal_events'] = 0
            self.clusters[cluster_id]['possible_abnormal_events'] = {}

            for possible_abnormal_event in self.possible_abnormal_events:

                possible_abnormal_event_index = self.events.index(
                    possible_abnormal_event)

                if centroid[possible_abnormal_event_index] != 0:

                    self.clusters[cluster_id]['num_possible_abnormal_events'] += 1
                    self.clusters[cluster_id]['possible_abnormal_events'][possible_abnormal_event] = [
                    ]

                    for log_sequence_id in self.clusters[cluster_id]['Log Sequence IDs']:
                        if self.log_sequences[log_sequence_id]['Representative Log Sequence'][possible_abnormal_event_index] == 1:
                            self.clusters[cluster_id]['possible_abnormal_events'][possible_abnormal_event].append(
                                log_sequence_id)

            self.clusters[cluster_id]['centroid'] = centroid.tolist()

            del self.clusters[cluster_id]['Log Sequence IDs']
            del self.clusters[cluster_id]['Events']


