import re

class LogParser():
    def __init__(self, input_file):
        self.input_file = input_file
        self.anonymized_data = []
        self.log_sequences = {}
        self.log_event = {}
        self.events = []
        
        self.WORD_REGEX = r'([a-zA-Z]+)\s?'
        self.PARAM_REGEX = r'\<*\>'

    def parse(self):
        self.anonymize()
        self.extract_events()
        self.get_representative_log_sequence()

        return self.events, self.log_sequences

    def anonymize(self):
        '''
            Takes the relevant data from the dataset and anonymizes dynamic tokens
            by replacing it with a <*> wildcard.

            The resulting data is stored in self.anonymized_data for later use.
        '''
        with open(self.input_file) as log_file:
            log_index = 0
            
            for log in log_file:
                cleaned_log = log.split(':', 1)  # Remove unnecessary data
                tokens = cleaned_log[1].split()
                log_template = ''

                for token in tokens:
                    if token[:5] == 'local' or token[:6] == 'remote':
                        token = token.split('/')[0] + '<*>'

                    elif token[:3] == 'blk':
                        blk_id = token

                        if blk_id not in self.log_sequences: self.log_sequences[blk_id] = {'Logs': [log_index]} 
                        else: self.log_sequences[blk_id]['Logs'].append(log_index)

                        token = '<*>'

                    elif token[0] == '/' or token[0].isnumeric() or token[:4] == 'java':
                        token = '<*>'

                    log_template += token + ' '

                self.anonymized_data.append(log_template.strip())
                log_index += 1

    def extract_events(self):
        for anonimized_log_index, anonimized_log in enumerate(self.anonymized_data):
            if anonimized_log not in self.events: self.events.append(anonimized_log)
            
            self.log_event[anonimized_log_index] = self.events.index(anonimized_log)

    def get_representative_log_sequence(self):
        for key, value in self.log_sequences.items():
            representative_log_sequence = [0] * len(self.events)
            for anonymized_log_index in value['Logs']:
                event_index = self.log_event[anonymized_log_index]
                
                if representative_log_sequence[event_index] == 0: representative_log_sequence[event_index] += 1

            self.log_sequences[key]['Representative Log Sequence'] = representative_log_sequence

   