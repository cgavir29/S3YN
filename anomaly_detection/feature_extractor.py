from log_parser import LogParser


class FeatureExtractor():
    def __init__(self, input_file):

        self.logParser = LogParser(input_file)
        self.logSequences = {}

    def extract(self):
        logs, events = self.logParser.parse()

        for log in logs:
            blk = log['blk']
            eventIndex = log['Event']

            if blk not in self.logSequences:
                self.logSequences[blk] = []

                for e in events:
                    self.logSequences[blk].append(0)

                self.logSequences[blk][eventIndex] = 1
            else:
                self.logSequences[blk][eventIndex] += 1

        return self.logSequences
