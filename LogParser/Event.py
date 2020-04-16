import hashlib

class Event():

    def __init__(self, logIdx, eventStr=""):
        
        self.id = hashlib.md5(eventStr.encode('utf-8')).hexdigest()[0:8]
        self.logs = [logIdx]
        self.eventStr = eventStr
        self.eventTokens = eventStr.split()
        self.merged = False

    def refresh_id(self):
        self.id = hashlib.md5(self.eventStr.encode('utf-8')).hexdigest()[0:8]
        
    def getEventStr(self):
        return self.eventStr