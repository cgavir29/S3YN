import re
import hashlib


class LogParser():
    def __init__(self, input_file):
        self.input_file = input_file
        self.anonymized_data = []
        self.blk_events = []
        self.events = {}
        self.bins = {}
        self.WORD_REGEX = r'([a-zA-Z]+)\s?'
        self.PARM_REGEX = r'\<*\>'

    def parse(self):
        self.anonymize()
        self.tokenize()
        self.categorize()

        return self.events, self.blk_events

    def anonymize(self):
        '''
            Takes the relevant data from the dataset and anonymizes dynamic tokens
            by replacing it with a <*> wildcard.

            The resulting data is stored in self.anonymized_data for later use.
        '''
        with open(self.input_file) as log_file:
            for log in log_file:
                cleaned_log = log.split(':', 1)  # remove unnecessary data
                tokens = cleaned_log[1].split()
                # params = []
                log_template = ''
                # blk = ''

                for token in tokens:
                    if token[0] == '/' or token[0].isnumeric() or token[:3] == 'blk':
                        # necessary?
                        if token[:3] == 'blk':
                            pass
                            # blk = token

                        token = '<*>'

                    log_template += token + ' '

                self.anonymized_data.append(log_template.strip())

        # with open(self.input_file, 'r') as log_file:

        #     for line in log_file.readlines():
        #         log_tokens = line.split()
        #         logTemplate = ''
        #         params = []
        #         blk = ''

        #         for token in log_tokens:

        #             if token[0] == '/' or token[0].isnumeric() or token[:3] == 'blk':
        #                 params.append(token)
        #                 if token[:3] == 'blk':
        #                     blk = token
        #                 token = '<*>'

        #             logTemplate += token + ' '

        #         self.logs.append({'LogTemplate': logTemplate,
        #                           'Params': params, 'blk': blk, 'Event': ''})

    def tokenize(self):
        '''
            After the data has been anonymized, this step takes care of separating it into 
            collections which are formed based on the number of words and params (dynamic tokens) in 
            each log.

            Aditional data, namely the 'events' key is added to ease the categorization step.
        '''
        for idx, log in enumerate(self.anonymized_data):
            num_of_words = len(re.findall(self.WORD_REGEX, log))
            num_of_params = len(re.findall(self.PARM_REGEX, log))

            key = f'{num_of_words}.{num_of_params}'  # Set key for that log -> 'w.p'

            if not self.bins.get(key):
                # Create an item in the dict if it doesn't exist already
                self.bins[key] = {
                    'logs': [idx],
                    'events': []
                }
            else:
                # Otherwise add to that existing item
                self.bins.get(key).get('logs').append(idx)

        # log_index = 0

        # for log in self.logs:

        #     if 'Logs' not in self.bins[(numTokens, numParams)]:

        #         self.bins[(numTokens, numParams)]['Logs'] = [log_index]

        #     else:

        #         self.bins[(numTokens, numParams)]['Logs'].append(log_index)

        #     log_index += 1

    def categorize(self):
        for key, val in self.bins.items():
            pass

        # for key in self.bins:

        #     binContent = self.bins[key]
        #     binContent['Events'] = []

        #     for log_index in binContent['Logs']:

        #         logTemplate = self.logs[log_index]['LogTemplate']
        #         matched = False

        #         for eventIndex in binContent['Events']:

        #             if logTemplate == self.events[eventIndex]:

        #                 matched = True
        #                 self.logs[log_index]['Event'] = eventIndex
        #                 break

        #         if not matched:

        #             eventIndex = hashlib.md5(
        #                 logTemplate.encode('utf-8')).hexdigest()[0:8]
        #             self.events[eventIndex] = logTemplate
        #             self.logs[log_index]['Event'] = eventIndex
        #             binContent['Events'].append(eventIndex)
