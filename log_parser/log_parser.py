import re

PAT_ANT = r'[0-9]{6}'
# PAT_ANT = '[0-9]{6}\s[0-9]{6}\s[0-9]{1,3}' # Fecha Hora ?
PAT_POS = r'([a-zA-Z]+)\s?'
# PAT_POS = r'([a-zA-Z]+\s)+?'
# PAT_POS = r'[a-zA-Z]+\s?[a-zA-Z]+'
DYNAMIC = r'[0-9]+|blk_-[0-9]+|([/]([0-9]+[.]?)+([:][0-9]+)?)'


def parse1(line):
    result = line.split(':', 1)
    ant = ' '.join(re.findall(PAT_ANT, result[0]))
    pos = ' * '.join(re.findall(PAT_POS, result[1]))

    return ant + ': ' + pos


class MyLogParser():
    def __init__(self, log_file):
        self.log_file = log_file
        self.log_data = None
        self.anonymized_data = []
        self.bins = {}  # '3.0' : []

    def parse(self):
        self.load_data()
        self.anonymize()
        self.tokenize()
        self.categorize()

    def load_data(self):
        with open(self.log_file) as file:
            # populate the list while removing '\n's
            self.log_data = [line.strip() for line in file]

    def anonymize(self):
        for line in self.log_data:
            result = line.split(':', 1)
            self.anonymized_data.append((re.sub(DYNAMIC, '<*>', result[1])))

    def tokenize(self):
        for line in self.anonymized_data:
            words = len(re.findall(PAT_POS, line))
            params = len(re.findall(r'\<*\>', line))

            # Figure key for that log_line
            key = f'{words}.{params}'
            # If <Key> doesn't exist then create it and add the line
            if not self.bins.get(key):
                self.bins[key] = [line]
            else:  # Append to the list value of that key
                self.bins.get(key).append(line)

    def categorize(self):
        for key, value in self.bins.items():
            for log_line in value:
                print(log_line)

    def reconcile(self):
        pass


if __name__ == '__main__':
    mlp = MyLogParser('HDFS_10.log')
    mlp.parse()
    print(mlp.bins)
    print(mlp.bins.keys())
