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
            for data in documents:
                document = self.translator.translate(data)
                print(document.name)
                print(document.code)
                print(document.price)
                print(document.capitalization)
                print(document.vol_24)
                print(document.total_vol)
                print(document.variance_24)
                print(document.variance_7)
                print('\n')
        except Exception as err:
            self.logger.error(err)
            raise err
