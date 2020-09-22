import scrapy
from push_redis import push_redis
from push_redis import get_redis_crawl



class JngpSpider(scrapy.Spider):
    name = 'crawlB'
    allowed_domains = []
    start_urls = []
    custom_settings = {
        'ITEM_PIPELINES': {'zhihu.pipelines.crawlBPipeline': 301}
    }

    def parse(self, response):
        this_machine = 'master'
        print('开始分布式爬虫')
        if this_machine == 'master':
            url = 'D:\\python\\PycharmProjects\\zhihu\\urlsFiles\\jngp.txt'
            push_redis(url,'crawlB_url')
        else:
            items = get_redis_crawl(self.name)
            for item in items:
                yield item

