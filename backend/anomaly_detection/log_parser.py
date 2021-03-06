import re

class LogParser():
    def __init__(self, input_file):
        self.input_file = input_file
        self.anonymized_data = []
        self.log_sequences = {}
        
        self.tagged_events = {}
        self.log_event = {}

        self.WORD_REGEX = r'([a-zA-Z]+)\s?'
        self.PARAM_REGEX = r'\<*\>'

    def parse(self):
        self.anonymize()
        self.extract_events()
        self.get_representative_log_sequence()

        return self.tagged_events, self.log_sequences

    def anonymize(self):
        '''
            Takes the relevant data from the dataset and anonymizes dynamic tokens
            by replacing it with a <*> wildcard.

            The resulting data is stored in self.anonymized_data for later use.
        '''
        with open(self.input_file) as log_file:
            log_index = 0
            
            for log in log_file:
                cleaned_log = log.split(':', 1) 
                
                type_event = cleaned_log[0].split()[3]
                tokens = cleaned_log[1].split()
                
                log_template = type_event + ':'

                for token in tokens:
                    if token[:5] == 'local':
                        token = token.split('/')[0] + '<*>'
                    
                    elif token[:6] == 'remote':
                        token = token.split('/')[0] + '<*>]'       

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
            
            del log_file

    def extract_events(self):        
        for anonimized_log_index, anonimized_log in enumerate(self.anonymized_data):
            
            typed_anonimized_log = anonimized_log.split(':', 1) 
            
            type_anonimized_log = typed_anonimized_log[0]
            str_anonimized_log = typed_anonimized_log[1]

            if str_anonimized_log not in self.tagged_events: 
                self.tagged_events[str_anonimized_log] = type_anonimized_log

            events = list(self.tagged_events.keys())

            self.log_event[anonimized_log_index] = events.index(str_anonimized_log) 

        del self.anonymized_data

    def get_representative_log_sequence(self):
        for key, value in self.log_sequences.items():
            representative_log_sequence = [0] * len(self.tagged_events.keys())
            
            for log_index in value['Logs']:
                event_index = self.log_event[log_index]
                
                if representative_log_sequence[event_index] == 0: representative_log_sequence[event_index] = 1

            self.log_sequences[key]['Representative Log Sequence'] = representative_log_sequence
            del self.log_sequences[key]['Logs']
   