class QuotationDocument(object):
    def __init__(self, name=None, code=None, price=None, capitalization=None, vol_24=None, total_vol=None, variance_24=None, variance_7=None):
        self.name = name
        self.code = code
        self.price = price
        self.capitalization = capitalization
        self.vol_24 = vol_24
        self.total_vol = total_vol
        self.variance_24 = variance_24
        self.variance_7 = variance_7

class QuotationReference(object):
    def __init__(self, document):
        self.document = QuotationDocument(
            document['name'],
            document['code'],
            document['price'],
            document['capitalization'],
            document['vol_24'],
            document['total_vol'],
            document['variance_24'],
            document['variance_7']
        )