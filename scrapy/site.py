from bs4 import Tag
from library.dataclass import Entry
from library.functions import get_title, get_float
from scrapy.base import Base

class site(Base):
    url_base = str

    def __init__(self):
        self.url_base = ''
        self.items_list = ['']
        self.url_text = '' 
        self.page_range = range(1)
        self.sites = self.get_url(self.url_base, self.items_list, self.url_text, self.page_range)
        self.revenda = 'site'
        
    @staticmethod
    def _get_products_from_site(site):
        return site.findAll('', attrs={'': ''})
   
    def _map_tag_to_product(
            self, 
            item: Tag
    ) -> Entry:
        
        title_tag = item.find('', attrs={'': ''})
        price_tag = item.find('', attrs={'': ''})

        title = get_title(title_tag)
        pricefloat_tag = get_float(price_tag)

        return Entry(
            sale=self.revenda,
            title=title,
            price=pricefloat_tag,
        )

