from application.service.ScrapingRowsService import SrapingRowsService
from application.translator.RowToDataTranslator import RowToDataTranslator
from infrastructure.configuration.Configuration import AppConfiguration

from infrastructure.repository.QuotationRepository import QuotationRepository

class StartMiningUseCase():
    def __init__(self):
        configuration = AppConfiguration()
        self.logger = configuration.getLogger(__name__)
        self.service = SrapingRowsService()
        self.translator = RowToDataTranslator()
        self.repository = QuotationRepository()

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(StartMiningUseCase, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def execute(self):
        try:
            rows = self.service.scrap()
            if (rows is not None):
                self.repository.clean()
                documents = [self.translator.translate(row) for row in rows]
                return [self.repository.save(document) for document in documents]                    
        except Exception as err:
            self.logger.error(err)
            raise err
        finally:
            self.repository.close()
