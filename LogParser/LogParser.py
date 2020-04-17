from collections import defaultdict
import hashlib

class LogParser():

    def __init__(self, inFile):

        self.inFile = inFile
        self.logs = []    
        self.events = defaultdict(dict)
        self.bins = defaultdict(dict)

    def parse(self):

        self.anonymize()
        self.tokenize()
        self.categorize()

        return self.logs, self.events

    def anonymize(self):

        with open(self.inFile, 'r') as logFile:
            for line in logFile.readlines():

                logTokens = line.split()
                
                logTemplate = ''
                params = []
                blk = ''
                
                for token in logTokens:

                    if token[0] == '/' or token[0].isnumeric() or token[:3] == 'blk': 
                        params.append(token)
                        if token[:3] == 'blk': blk = token
                        token = '<*>'

                    logTemplate += token + ' '

                self.logs.append({'LogTemplate': logTemplate, 'Params': params, 'blk': blk, 'Event': ''})
                 
                
    def tokenize(self):

        logIndex = 0

        for log in self.logs:

            numParams = len(log['Params'])
            numTokens = len(log['LogTemplate'].split()) 

            if 'Logs' not in self.bins[(numTokens, numParams)]:

                self.bins[(numTokens, numParams)]['Logs'] = [logIndex]

            else: 
                
                self.bins[(numTokens, numParams)]['Logs'].append(logIndex)

            logIndex += 1

    def categorize(self):

        for key in self.bins:
            
            binContent = self.bins[key]
            binContent['Events'] = []

            for logIndex in binContent['Logs']:
            
                logTemplate = self.logs[logIndex]['LogTemplate']
                matched = False

                for eventIndex in binContent['Events']:
                
                    if logTemplate == self.events[eventIndex]:
                    
                        matched = True
                        self.logs[logIndex]['Event'] = eventIndex
                        break
            
                if not matched:
                    
                    eventIndex = hashlib.md5(logTemplate.encode('utf-8')).hexdigest()[0:8]
                    self.events[eventIndex] = logTemplate
                    self.logs[logIndex]['Event'] = eventIndex 
                    binContent['Events'].append(eventIndex)
    