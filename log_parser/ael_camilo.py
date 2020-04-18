import re
from datetime import datetime
import AEL as logpai_ael


class Event:
    def __init__(self, log_index, event_str=''):
        self.id = None


class AEL:
    def __init__(self, logfile, minEventCount=2, merge_percent=1, 
                 rex=[], keep_para=True):
        self.logfile = logfile
        self.rex = rex
        self.minEventCount = minEventCount
        self.merge_percent = merge_percent
        self.df_log = None
        self.merged_events = []
        self.bins = {}
        self.keep_para = keep_para

    def parse(self, logfile):
        start_time = datetime.now()
        print('Parsing file: ' + self.logfile)
        self.load_data()
        self.tokenize()
        self.categorize()
        self.reconcile()
        print('Parsing done. [Time taken: {!s}]'.format(datetime.now() - start_time))

    def load_data(self):
        log_messages = []
        line_count = 0

        with open(self.logfile) as file:
            for line in file.readlines():
                try:
                    pass
                except:
                    pass

    def tokenize(self):

        pass

    def categorize(self):
        pass

    def reconcile(self):
        pass

    def generate_logformat_regex(self, logformat):
        ''' 
        Function to generate regular expression to split log messages

        '''
        headers = []
        splitters = re.split(r'(<[^<>]+>)', logformat)
        regex = ''
        for k in range(len(splitters)):
            if k % 2 == 0:
                splitter = re.sub(r' +', r'\s+', splitters[k])
                regex += splitter
            else:
                header = splitters[k].strip('<').strip('>')
                regex += '(?P<%s>.*?)' % header
                headers.append(header)
        regex = re.compile('^' + regex + '$')
        return headers, regex


if __name__ == '__main__':
    # log_file = input('Log file to analyze > ')

    # ael1 = AEL(log_file)
    lpael1 = logpai_ael.LogParser('./', './', ':')
    lpael1.parse('HDFS_1K.log')
