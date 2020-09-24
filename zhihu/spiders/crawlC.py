import scrapy
from push_redis import get_redis_crawl
from push_redis import push_redis



class ExampleSpider(scrapy.Spider):
    name = 'crawlC'
    allowed_domains = []
    start_urls = []
    custom_settings = {
        'ITEM_PIPELINES': {'zhihu.pipelines.crawlCPipeline': 300}
    }

    def parse(self, response):
        this_machine = 'master'
        print('开始分布式爬虫')
        if this_machine == 'master':
            url = r"D:\python\PycharmProjects\zhihu\zhihu\sources\jndp.txt"
            push_redis(url,'crawlC_url')
        else:
            items = get_redis_crawl(self.name)
            for item in items:
                yield item

