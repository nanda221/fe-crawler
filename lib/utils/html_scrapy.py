import re
from urllib import parse
from lxml.html import soupparser, fragment_fromstring, document_fromstring
from lxml.etree import tostring

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
        html = download.html(url, {'User_agent': 'scrape page links'}, 3)
    else:
        html = url
    if not html:
        print(
            '[scrape_links]: error ocurrs when approach target url: \033[33m{0}\033[0m'.
            format(url))
        return {'html': html, 'links': []}

    link_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', re.IGNORECASE)
    # use the lamda trick, map returns a iterator object, so we use list method to convert.
    links = list(map(_urlparse, link_regex.findall(html)))
    # print(links)
    if regex:
        links = list(filter(lambda l: re.match(regex, l), links))
    return {'html': html, 'links': links}


def html_parse_by_soupparser(url, need_download=True):
    '''
    beautiful soup(bs4) should used when the html is really broken, or handle the encoding problems.
    see "http://lxml.de/lxmlhtml.html" for more details.
    '''
    if (need_download):
        html = download.html(url, {'User_agent': 'scrape'}, 3)
    else:
        html = url
    e_tree = soupparser.fromstring(html)
    print(tostring(e_tree, pretty_print=False).strip().decode())
    return soupparser.fromstring(html)


def html_parse_by_css_selector(url, css_selector, need_download=True):
    '''
    use the dafault parse method is faster.
    see "http://lxml.de/lxmlhtml.html" for more details.
    '''

    if (need_download):
        html = download.html(url, {'User_agent': 'scrape'}, 3)
    else:
        html = url
    # e_tree = fragment_fromstring(html, 'section')
    e_tree = document_fromstring(html)
    # print(tostring(e_tree, pretty_print=False).strip().decode())
    tags = e_tree.cssselect(css_selector)
    return [tag.get('href') for tag in tags]


# if __name__ == '__main__':
# print(scrape_page_title(
#     'https://nanda221.github.io/2017/01/04/python-colorful-printer.html'))
# html_parse('https://nanda221.github.io/2017/01/04/python-colorful-printer.html')
