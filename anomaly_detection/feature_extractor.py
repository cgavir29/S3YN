from log_parser import LogParser


class FeatureExtractor():
    def __init__(self, input_file):
        self.log_parser = LogParser(input_file)
        self.log_sequences = {}

    def extract(self):
        events, logs = self.log_parser.parse() # events, blk_events

        for log in logs:
            blk = log['blk']
            event_index = log['event']

            if blk not in self.log_sequences:
                self.log_sequences[blk] = []

                for e in events:
                    self.log_sequences[blk].append(0)

                self.log_sequences[blk][event_index] = 1
            else:
                self.log_sequences[blk][event_index] += 1

        return self.log_sequences
