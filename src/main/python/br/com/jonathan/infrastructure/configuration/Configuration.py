import yaml
import logging

from infrastructure.data.property.MongoDBProperty import MongoDBProperty

YML_PROPERTIES = 'src/main/resources/application.yml'

class AppConfiguration():
    def __init__(self):
        self.configure()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(AppConfiguration, cls).__new__(cls, *args, **kwargs)
        return cls._instance
    
    def configure(self):
        logging.basicConfig(level=logging.DEBUG)
        stream = open(YML_PROPERTIES, "r")
        docs = yaml.load_all(stream)
        for doc in docs:
            for k,v in doc.items():
                if k == 'mongo':
                    self.mongo = MongoDBProperty(
                        self.env(v, 'host'), 
                        self.env(v, 'port'), 
                        self.env(v, 'username'),
                        self.env(v, 'password'))

    def env(self, data, key):
        try:
            return data[key]
        except:
            return None
    
    def getMongoDBProperty(self):
        return self.mongo

    def getLogger(self, name):
        return logging.getLogger(name)