import re
from urllib import parse

from .download import download


def scrape_page_title(url, need_download=True):
    if (need_download):
        html = download.html(url, {'User_agent': 'scrape page title'}, 3)
    else:
        html = url
    if not html:
        print(
            '[scrape_page_title]: error ocurrs when approach target url: \033[33m{0}\033[0m'.
            format(url))
        return None
    title = re.findall('<title>([\s\S]*?)</title>', html)
    if len(title):
        return title[0]
    else:
        return None


def scrape_links(url, regex=None, need_download=True):
    def _urlparse(relative_url):
        return parse.urljoin(url, relative_url)

    if (need_download):
        html = download.html(url, {'User_agent': 'scrape page title'}, 3)
    else:
        html = url
    if not html:
        print(
            '[scrape_links]: error ocurrs when approach target url: \033[33m{0}\033[0m'.
            format(url))
        return {'html': html, 'links': []}

    link_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    # use the lamda trick, map returns a iterator object, so we use list method to convert.
    links = list(
        map(_urlparse, link_regex.findall(html)))
    # print(links)
    if regex:
        links = list(filter(lambda l: re.match(regex, l), links))
    return {'html': html, 'links': links}


# print(scrape_page_title('https://nanda221.github.io/2017/01/04/python-colorful-printer.html'))
