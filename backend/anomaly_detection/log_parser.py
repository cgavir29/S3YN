import re


class LogParser():
    def __init__(self, input_file):
        self.input_file = input_file
        self.anonymized_data = []
        self.blk_events = []
        self.events = []
        self.bins = {}
        self.WORD_REGEX = r'([a-zA-Z]+)\s?'
        self.PARAM_REGEX = r'\<*\>'

    # --------------------------------------------------------------------------------------------
    def parse(self):
        self.anonymize()
        self.tokenize()
        self.categorize()

        return self.events, self.blk_events

    # --------------------------------------------------------------------------------------------
    def anonymize(self):
        '''
            Takes the relevant data from the dataset and anonymizes dynamic tokens
            by replacing it with a <*> wildcard.

            The resulting data is stored in self.anonymized_data for later use.
        '''
        with open(self.input_file) as log_file:
            for log in log_file:
                cleaned_log = log.split(':', 1)  # Remove unnecessary data
                tokens = cleaned_log[1].split()
                log_template = ''

                for token in tokens:
                    if token[0] == '/' or token[0].isnumeric() or token[:3] == 'blk':
                        if token[:3] == 'blk':
                            # Register blk and to-be determined event
                            self.blk_events.append([token, -1])

                        token = '<*>'

                    log_template += token + ' '

                self.anonymized_data.append(log_template.strip())

    # --------------------------------------------------------------------------------------------
    def tokenize(self):
        '''
            After the data has been anonymized, this step takes care of separating it into
            collections which are formed based on the number of words and params (dynamic tokens)
            in each log.

            Aditional data, namely the 'events' key is added to ease the categorization step.
        '''
        for idx, log in enumerate(self.anonymized_data):
            num_of_words = len(re.findall(self.WORD_REGEX, log))
            num_of_params = len(re.findall(self.PARAM_REGEX, log))

            # Set key for that log -> 'w.p'
            key = f'{num_of_words}.{num_of_params}'

            if not self.bins.get(key):
                # Create an item in the dict if it doesn't exist already
                self.bins[key] = {
                    'logs': [idx],
                    'events': []
                }
            else:
                # Otherwise add to that existing item
                self.bins.get(key).get('logs').append(idx)

    # --------------------------------------------------------------------------------------------
    def categorize(self):
        '''
            Determines the resulting events in the data set and adds them to the to each bin 
            as well as to the self.events list.

            It also overrides the self.blk_events index (-1) so it references an event in the
            self.events list.
        '''
        for value in self.bins.values():
            for log_index in value.get('logs'):
                log_template = self.anonymized_data[log_index]

                if log_template in self.events:
                    event_index = self.events.index(log_template)
                    self.blk_events[log_index][1] = event_index
                else:
                    self.events.append(log_template)
                    event_index = len(self.events) - 1
                    value.get('events').append(event_index)
                    self.blk_events[log_index][1] = event_index
