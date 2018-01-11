from ..utils import html_scrapy as scrape

if None:
    print(1)


class Link_Deep_Crawler:
    # def __init__(self):

    def crawl(self, url, regex=None):
        crawl_queue = [url]
        crawled_set = set(crawl_queue)
        while len(crawl_queue):
            url = crawl_queue.pop()
            res = scrape.scrape_links(url)
            if 'links' in res and len(res['links']):
                for link in res['links']:
                    # the second parameter informs the html is ready, no need to download
                    title = scrape.scrape_page_title(res['html'], False)
                    print('URL：{0} | TITLE: {1}'.format(link, title))
                    if link not in crawled_set:
                        crawl_queue.append(link)
                    # set won't add the same item twice, so we can add links out of the if block below
                    crawled_set.add(link)


crawler = Link_Deep_Crawler().crawl

# print(download.html('http://www.baidu21321321.com', None, 3))
# print(download.html('http://httpstat.us/500'))
# print(download.html('http://www.baidu.com'))
# print(download.robots('http://www.baidu.com/robots.txt'))
