# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhihuItem(scrapy.Item):
     id = scrapy.Field()
     name = scrapy.Field()
     kaijiang_data = scrapy.Field()
     kaijiang_numb = scrapy.Field()

class GopinItem(scrapy.Item):
     id = scrapy.Field()
     name = scrapy.Field()
     qihao = scrapy.Field()
     kaijiang_day = scrapy.Field()
     kaijiang_data = scrapy.Field()
     kaijiang_numb = scrapy.Field()


class ShishicaiItem(scrapy.Item):
     #id
     id = scrapy.Field()
     #名称
     name = scrapy.Field()
     #期数
     kaijiang_data = scrapy.Field()
     #号码
     kaijiang_numb = scrapy.Field()
     #开奖日期
     kaijiang_day = scrapy.Field()


