class MongoDBProperty(object):
    def __init__(self, host, port, username = None, password = None):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
