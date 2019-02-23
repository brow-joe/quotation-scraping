from infrastructure.configuration.Configuration import AppConfiguration
from domain.document.QuotationDocument import QuotationDocument, QuotationReference

class DocumentDataTranslator():
    def __init__(self):
        configuration = AppConfiguration()
        self.logger = configuration.getLogger(__name__)

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(DocumentDataTranslator, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def translate(self, document):
        try:
            return QuotationReference(document).document
        except Exception as err:
            self.logger.error(err)
            raise err
