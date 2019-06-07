import urllib.request
from urllib.error import HTTPError, URLError
import os
import numpy as np
from bs4 import BeautifulSoup
import argparse

class MangaScraper():

    def __init__(self, data_dir):
        self.data_dir = data_dir
        _, self.name = os.path.split(self.data_dir)
        self.failed = list()
        if not os.path.exists(self.data_dir):
            os.mkdir(self.data_dir)

    def search_image(self, chap_nb, html):
        soup = BeautifulSoup(html, "lxml")
        user_agent = 'Mozilla/5.0'
        headers = {'User-Agent': user_agent }
        next_page = None
        for page in soup.find_all('a', attrs={'class': 'btn btn-warning'}):
            next_page = page
        for i, img in enumerate(soup.find_all('img', attrs={'class':'pages__img'})):
            fn = '{}-{}-{:02d}.png'.format(self.name, chap_nb, i)
            path = os.path.join(self.data_dir, fn)
            if not os.path.exists(path):
                print(fn)
                try:
                    request = urllib.request.Request( url=img['src'], headers=headers )
                    openurl = urllib.request.urlopen(request)
                    content = openurl.read()
                    with open(path, 'wb') as f:
                        f.write(content)
                except (HTTPError, URLError):
                    self.failed.append((fn, img['src']))
                    print(img['src'])
                    print('KO') 
        return next_page['href']

    def crawl_url(self, url):
        chap_nb = url.split('-')[-1][:-1]
        try:
            user_agent = 'Mozilla/5.0'
            headers = {'User-Agent': user_agent }
            request = urllib.request.Request( url=url, headers=headers )
            print(url)
            openurl = urllib.request.urlopen(request)
            html = openurl.read()
            next_url = self.search_image(chap_nb, html)
            self.crawl_url(next_url)
        except (HTTPError, URLError):
            print('KO')

    def run(self, url):
        self.crawl_url(url)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('url', help='starting point')
    parser.add_argument('data_dir', help='data directory')
    args = parser.parse_args()

    crawer = MangaScraper(args.data_dir)
    crawer.run(args.url)