import math

class FeatureExtractor():
    def __init__(self, log_sequences, events):
        self.log_sequences = log_sequences
        self.events = events
        self.events_idf_value = []

    def extract(self):
        self.calculate_idf()
        self.generate_features_vector()

        return self.log_sequences
        
    def calculate_idf(self):       
        log_sequence_ids = list(self.log_sequences.keys())
        num_log_sequences = len(log_sequence_ids)

        for event_index in range(len(self.events)):
            num_event_appearances = 0
    
            for log_sequence_id in log_sequence_ids:
                if self.log_sequences[log_sequence_id]['Representative Log Sequence'][event_index] == 1: num_event_appearances += 1
            
            self.events_idf_value.append(math.log(num_log_sequences/num_event_appearances))

    def generate_features_vector(self):
        log_sequence_ids = list(self.log_sequences.keys())

        for log_sequence_id in log_sequence_ids:
            features_vector = [0] * len(self.events)
            
            representative_log_sequence = self.log_sequences[log_sequence_id]['Representative Log Sequence']
            for event_index in range(len(representative_log_sequence)):
                if representative_log_sequence[event_index] == 1:
                    features_vector[event_index] = self.events_idf_value[event_index]

            self.log_sequences[log_sequence_id]['Features Vector'] = features_vector