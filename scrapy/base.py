from typing import List
from bs4 import BeautifulSoup, Tag
import requests
from library.dataclass import Entry
import logging

class Base:
    resale: str

    @staticmethod
    def get_url(url_base: str, items_list: list, url_text: str, page_range: range) -> List[BeautifulSoup]:
        sites = []

        for product in items_list:
            for page in page_range:
                headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
                url_product = f'{url_base}{product}{url_text}{page}'
                response = requests.get(url_product, headers=headers)
                site = BeautifulSoup(response.text, 'html.parser')
                sites.append(site)
        
        return sites

    def _map_tag_to_product(
        self,
        product: Tag
    ) -> Entry:
    
        NotImplementedError

    @staticmethod
    def _get_products_from_site(site):
      
        NotImplementedError

    def get_entrys(self) -> List[Entry]:
        entrys = []
        for site in self.sites:
            products = self._get_products_from_site(site)
            for product in products:
                entry = self._map_tag_to_product(product)
                if entry:
                    entrys.append(
                        entry
                    )
        entrys_validate = [
            entry for entry in entrys
            if entry is not None
        ]
        logging.info(
            f'{len(entrys_validate)} produtos encontrados '
            f'para o site {self.resale}'
        )

        return entrys
