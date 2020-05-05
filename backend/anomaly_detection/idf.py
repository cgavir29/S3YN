import math

class IDF():
    def __init__(self, log_sequences):
        self.log_sequences = log_sequences
        self.NTs = []
        self.IDFs = []
        self.events = []
        self.N = 0
        self.aux = 0;

    def getIDF(self):
        self.calculateNT()

        for idf in range(0, len(self.NTs)):
            self.IDFs.append(math.log(self.N/self.NTs[idf]))

        return self.IDFs

    def calculateNT(self):
        self.N = len(self.log_sequences)

        for blk in self.log_sequences:
            self.events = self.log_sequences.get(blk)
            for event in range(0, len(self.events)):
                if self.aux != 1:
                    self.NTs.append(self.aux)
            self.aux = 1

            for event in range(0, len(self.events)):
                if self.events[event] > 0:
                    self.NTs[event] += 1

