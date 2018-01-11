from lib.services.link_deep_crawler import crawler as cr
from lib.utils import html_scrapy
from lib.services import mongo_client
if __name__ == '__main__':
    # cr('https://www.cainiao.com')
    # html_scrapy.html_parse_by_soupparser('https://scs.cainiao-inc.com/site/index.html')
    # links = html_scrapy.html_parse_by_css_selector('https://www.cainiao.com',
    #                                                '.slider-item a')
    client = mongo_client.connect()
    db = client.test1
    print(db.my_collection.insert_one({"x": 10}).inserted_id)
    print(db.my_collection123123)
    