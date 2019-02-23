from infrastructure.configuration.Configuration import AppConfiguration

import requests
from bs4 import BeautifulSoup

class SrapingRowsService():
    def __init__(self):
        configuration = AppConfiguration()
        self.logger = configuration.getLogger(__name__)
        self.url = 'https://br.investing.com/crypto/currencies/'
        self.headers = {
            'User-Agent': 'Chrome/39.0.2171.95'
        }

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(SrapingRowsService, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def scrap(self):
        try:
            request = requests.get(self.url, headers=self.headers)
            page = request.text
            if (page is not None):
                parse = BeautifulSoup(page, 'html.parser')
                section = parse.find(id='fullColumn')
                if (section is not None):
                    table = section.find('table')
                    if (table is not None):
                        body = table.find('tbody')
                        if (body is not None):
                            rows = body.find_all('tr')
                            if (rows is not None):
                                return [row.find_all("td") for row in rows]
        except Exception as err:
            self.logger.error(err)
            raise err
