from infrastructure.configuration.Configuration import AppConfiguration

from application.translator.DocumentDataTranslator import DocumentDataTranslator
from infrastructure.repository.QuotationRepository import QuotationRepository

class ReportUseCase():
    def __init__(self):
        configuration = AppConfiguration()
        self.logger = configuration.getLogger(__name__)
        self.translator = DocumentDataTranslator()
        self.repository = QuotationRepository()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(ReportUseCase, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def execute(self):
        try:
            documents = self.repository.findAll()
            if (documents is not None):
                return [self.translator.translate(document) for document in documents]
        except Exception as err:
            self.logger.error(err)
            raise err
