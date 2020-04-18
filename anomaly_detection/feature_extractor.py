from log_parser import LogParser

class FeatureExtractor():
    def __init__(self, input_file):
        self.log_parser = LogParser(input_file)
        self.log_sequences = {}

    def extract(self):
        group_events_by_blk()

        for blk in self.log_sequences:
            frequency_of_events = self.log_sequences[blk]

            print('For block ' + blk + ' the event vector is ' + ', '.join(frequency_of_events))



    def group_events_by_blk(self):
        events, blk_events = self.log_parser.parse() # events, blk_events

        num_events = len(events)

        for blk_event in blk_events:
            blk = blk_event[0]
            event_index = blk_event[1]

            if blk not in self.log_sequences:
                self.log_sequences[blk] = [0] * num_events
                self.log_sequences[blk][event_index] = 1
            else:
                self.log_sequences[blk][event_index] += 1
