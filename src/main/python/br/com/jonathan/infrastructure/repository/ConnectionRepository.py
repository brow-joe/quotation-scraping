from pymongo import MongoClient

from infrastructure.configuration.Configuration import AppConfiguration

class ConnectionRepository():
    def __init__(self):
        configuration = AppConfiguration()
        repository = configuration.getMongoDBProperty()
        self.logger = configuration.getLogger(__name__)
        try:
            if (repository.username is not None):
                self.db = MongoClient(
                    host=repository.host, 
                    port=repository.port, 
                    username=repository.username, 
                    password=repository.password)
            else:
                self.db = MongoClient(
                    host=repository.host, 
                    port=repository.port)
        except:
            pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(ConnectionRepository, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    def client(self):
        if self.db is not None:
            return self.db.coins
        else:
            raise 'No client connection'

    def close(self):
        try:
            self.db.close()
        except:
            pass
