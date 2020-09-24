import scrapy
from push_redis import push_redis
from push_redis import get_redis_crawl
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime



class CrawlaSpider(scrapy.Spider):
    name = 'crawlA'
    allowed_domains = ['kaijiang.aicai.com']
    start_urls = ['http://kaijiang.aicai.com/']
    custom_settings = {
        'ITEM_PIPELINES': {'zhihu.pipelines.crawlAPipeline': 301}
    }


    def parse(self, response):
        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        scheduler = BlockingScheduler()
        scheduler.add_job(func=dingshi, trigger='interval', seconds=60)
        scheduler.start()


def dingshi():
    this_machine = 'master'
    print('开始分布式爬虫')
    if this_machine == 'master':
        url = r"D:\python\PycharmProjects\zhihu\zhihu\sources\adr"
        push_redis(url, 'crawlA_url')
    else:
        items = get_redis_crawl('crawlA')
        for item in items:
            yield item


