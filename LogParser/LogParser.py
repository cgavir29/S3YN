from Event import Event

from collections import defaultdict

class LogParser():

    def __init__(self, inFile):

        self.inFile = inFile
        self.logs = []
        self.logParams = []
        self.bins = defaultdict(dict)    

    def parse(self):

        self.anonymize()
        self.tokenize()
        self.categorize()

        eventCounter = 0
        conflictCounter = 0

        for key in self.bins:

            binContent = self.bins[key]

            for event in binContent['Events']: 
                print(event.getEventStr())
                eventCounter += 1
            
            if len(binContent['Events']) > 1: 
                conflictCounter += 1
                for k in range(len(binContent['Events'])): print('*') 

        print(str(len(self.logs)) + ' log lines.')
        print(str(eventCounter) + " events found.")
        print(str(conflictCounter) + " conflicts found.")


    def anonymize(self):

        with open(self.inFile, 'r') as logFile:
            for line in logFile.readlines():

                logTokens = line.split()
                
                abstractLog = ''
                params = []
                
                for token in logTokens:

                    if token[0] == '/' or token[0].isnumeric() or token[:3] == 'blk': 
                        params.append(token)
                        token = '<*>'

                    abstractLog += token + ' '

                self.logs.append(abstractLog)
                self.logParams.append(params)
                
    def tokenize(self):

        logIdx = 0

        for logStr in self.logs:

            paramCounter = 0
            tokens = logStr.split() 

            for token in tokens: 
                if token == "<*>": paramCounter += 1

            if 'Logs' not in self.bins[(len(tokens), paramCounter)]: 
                self.bins[(len(tokens), paramCounter)]['Logs'] = [logIdx]
            else: 
                self.bins[(len(tokens), paramCounter)]['Logs'].append(logIdx)

            logIdx += 1

    def categorize(self):

        for key in self.bins:
            
            binContent = self.bins[key]
            binContent['Events'] = []

            for logIdx in binContent['Logs']:
            
                logStr = self.logs[logIdx]
                matched = False

                for event in binContent['Events']:
                
                    if logStr == event.eventStr:
                    
                        matched = True
                        event.logs.append(logIdx)
                        break
            
                if not matched:
                    binContent['Events'].append(Event(logIdx, logStr))
    