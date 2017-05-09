import requests
from lxml import etree
from verbose_octo_goggles.core import SkipItem
from verbose_octo_goggles.reader.base import BaseReader
from verbose_octo_goggles.reader.rss import BaseRssReader


class HabrHubsReader(BaseReader):
    base_url = 'https://habrahabr.ru/rss/hubs'
    hubs = [
        'all',
    ]

    def data_stream(self):
        for hub in self.hubs:
            yield '{base_url}/{hub_name}'.format(
                base_url=self.base_url,
                hub_name=hub
            )

    def process_unit(self, unit):
        res = requests.get(unit)
        if res.status_code == 200:
            return etree.fromstring(res.content)
        else:
            raise SkipItem


class HabrRSSAllReader(BaseRssReader):
    items_xpath = '//channel/item'

    def get_sources(self):
        habr_reader = HabrHubsReader()
        for each in habr_reader:
            yield each
