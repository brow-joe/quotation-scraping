from infrastructure.configuration.Configuration import AppConfiguration
from domain.document.QuotationDocument import QuotationDocument

class RowToDataTranslator():
    def __init__(self):
        configuration = AppConfiguration()
        self.logger = configuration.getLogger(__name__)

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(RowToDataTranslator, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def translate(self, row):
        try:
            _, _, name, code, price, capitalization, vol_24, total_vol, variance_24, variance_7 = row
            return QuotationDocument(
                name.get_text(), 
                code.get_text(), 
                price.get_text(), 
                capitalization.get_text(), 
                vol_24.get_text(), 
                total_vol.get_text(), 
                variance_24.get_text(), 
                variance_7.get_text()
            )
        except Exception as err:
            self.logger.error(err)
            raise err
