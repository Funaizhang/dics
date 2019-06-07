import urllib.request
from urllib.error import HTTPError, URLError
import os
import numpy as np
from bs4 import BeautifulSoup
import argparse

class MangaScraper():

    def __init__(self, data_dir, begin, end):
        self.data_dir = data_dir
        self.urls = ['https://www.thiswaifudoesnotexist.net/example-{}.jpg'.format(x) for x in range(begin, end + 1)]
        if not os.path.exists(self.data_dir):
            os.mkdir(self.data_dir)

    def crawl_url(self, url, i):
        fn = '{}/{}.png'.format(self.data_dir, i)
        try:
            user_agent = 'Mozilla/5.0'
            headers = {'User-Agent': user_agent }
            request = urllib.request.Request( url=url, headers=headers )
            print(url)
            openurl = urllib.request.urlopen(request)
            content = openurl.read()
            with open(fn, 'wb') as f:
                f.write(content)

        except (HTTPError, URLError):
            print('KO')

    def run(self):
        for i, url in enumerate(self.urls):
            self.crawl_url(url, i)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--begin', type=int, default=0, help='starting image number')
    parser.add_argument('--end', type=int, help='end image number')
    parser.add_argument('--data-dir', help='data directory')
    args = parser.parse_args()

    crawer = MangaScraper(args.data_dir, args.begin, args.end)
    crawer.run()