from dateutil.parser import parse
from verbose_octo_goggles.importer.base import BaseImporter

from reddit.adapter import EntryAdapter
from reddit.reader import RedditRssReader


class RedditImporter(BaseImporter):
    reader_class = RedditRssReader
    adapter_class = EntryAdapter

    def wrangle(self, item):
        root, item = item
        namespace = '{%s}' % root.nsmap[None]
        get_node = lambda node, name: node.find('{}{}'.format(namespace, name))

        res = {
            'pk': get_node(item, 'id').text,
            'author': {
                'pk': get_node(get_node(item, 'author'), 'name').text,
                'uri': get_node(get_node(item, 'author'), 'uri').text
            },
            'category': {
                'pk': get_node(item, 'category').get('term')
            },
            'title': get_node(item, 'title').text,
            'content': get_node(item, 'content').text,
            'link': get_node(item, 'link').get('href'),
            'updated': parse(get_node(item, 'updated').text)
        }

        return res
