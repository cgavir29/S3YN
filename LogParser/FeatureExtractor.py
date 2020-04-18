from LogParser import LogParser

from collections import defaultdict

class FeatureExtractor():

    def __init__(self, inFile):

        self.logParser = LogParser(inFile)
        self.logSequences = defaultdict(dict)

    def extract(self):

        logs, events = self.logParser.parse()

        for log in logs:

            blk = log['blk']
            eventIndex = log['Event']

            if blk not in self.logSequences: 
                    
                self.logSequences[blk] = []
                
                for e in events: self.logSequences[blk].append(0)
                
                self.logSequences[blk][eventIndex] = 1

            else:

                self.logSequences[blk][eventIndex] += 1 

        return self.logSequences
            