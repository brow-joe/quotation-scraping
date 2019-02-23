from infrastructure.repository.ConnectionRepository import ConnectionRepository

class QuotationRepository():
    def __init__(self):
        self.repository = ConnectionRepository()
        self.client = self.repository.client().quotation

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(QuotationRepository, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def close(self):
        try:
            self.repository.close()
        except:
            pass
    
    def clean(self):
        self.client.remove({})
            
    def save(self, document):
        if (document is not None):
            document = document.__dict__
            return self.client.save(document)

    def findAll(self):
        return self.client.find({})
