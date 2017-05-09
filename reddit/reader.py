from verbose_octo_goggles.reader.http import XmlFromHttpReader
from verbose_octo_goggles.reader.rss import BaseRssReader


class RedditSourceReader(XmlFromHttpReader):
    def data_stream(self):
        yield 'https://www.reddit.com/r/news/.rss'


class RedditRssReader(BaseRssReader):

    def extract_items_from_xml(self, etree_root):
        return etree_root.findall('{http://www.w3.org/2005/Atom}entry')

    def get_sources(self):
        reddit_reader = RedditSourceReader()
        for source in reddit_reader:
            yield source
