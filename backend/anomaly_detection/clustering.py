import numpy as np # para realizar calculos avanzados
import pandas as pd # para el analisis de datos

import scipy.cluster.hierarchy as sch
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster

class Clustering():
    def __init__(self, feature_vectors):
        self.feature_vectors = feature_vectors
        
        self.list_feature_vectors = []
        
        for key in self.feature_vectors: self.list_feature_vectors.append(self.feature_vectors[key])
        
        self.array_feature_vectors = np.array(self.list_feature_vectors)

    def cluster(self):
        # creando diagrama del cluster jerárquico
        clustering_jerarquico = linkage(self.array_feature_vectors, 'ward') # se utiliza el metodo ward para agripar los clusters
        
        clusters = fcluster(clustering_jerarquico, t=2, criterion ='distance') # t altura de corte en en dendogram

        print(clusters)