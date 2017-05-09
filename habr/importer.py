from dateutil.parser import parse
from verbose_octo_goggles.core import BaseImporter

from habr.adapter import ArticleAdapter
from habr.reader import HabrRSSAllReader


class HabrImporter(BaseImporter):
    reader_class = HabrRSSAllReader
    adapter_class = ArticleAdapter

    def wrangle(self, item):
        etree_root, item = item

        link = item.find('link').text
        return {
            'pk': int(link.split('/')[-2]),
            'creator': {
                'pk': item.find('dc:creator', namespaces=etree_root.nsmap).text
            },
            'pub_date': parse(item.find('pubDate').text),
            'link': link,
            'title': item.find('title').text,
            'description': item.find('description').text,
            'categories': self.wrangle_categories(item)
        }

    def wrangle_categories(self, item):
        return map(lambda cat: {'pk': cat.text}, item.xpath('category'))


