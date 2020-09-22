import scrapy
import requests
from bs4 import BeautifulSoup
import re
from scrapy.utils.project import get_project_settings
import redis
from lxml import etree
from items import ZhihuItem

#redis
settings = get_project_settings()
r = redis.StrictRedis(host=settings['REDIS_HOST'],
                      port=settings['REDIS_PORT'],
                      password=settings['REDIS_PASSWORD'])


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['www.8200.cn']
    start_urls = ['https://www.8200.cn/df61/']

    def parse(self, response):
        this_machine = 'master1'
        print('开始分布式爬虫')
        if this_machine == 'master':
            link_list = []
            with open('D:\\python\\PycharmProjects\\zhihu\\jndp.txt', 'r') as file:
                url_list = file.readlines()
                for eachone in url_list:
                    link = re.findall('：(.*)', eachone)[0]
                    link_list.append(link)
                    r.lpush('url', link)
                    if len(link_list) == 100:
                        break
        else:
            while True:
                try:
                    url = r.lpop('url')
                    try:
                        response = requests.get(url)
                        html = etree.HTML(response.text)
                        # 名字
                        name = html.xpath('//a[@class="strong"]/text()')
                        id = match_id(name[0])
                        # print(name)
                        # 期数
                        kaijiang_data = html.xpath('//div[@class="kjhinfo"]/label/strong/text()')
                        # print(kaijiang_data)
                        # 开奖号码
                        kaijiang_numb = html.xpath('//label[@class ="boll"]/span/text()')
                        # print(kaijiang_numb)
                        item = ZhihuItem()
                        item['id'] = id
                        item['name'] = name[0]
                        item['kaijiang_data'] = kaijiang_data[0]
                        str = ''
                        for i in kaijiang_numb:
                            str += i
                        print(str)
                        item['kaijiang_numb'] = str
                        yield item
                    except Exception as e:
                        print("error")
                        break
                except Exception as e:
                    print(e)
                    break


def match_id(str):
    id = 0
    if str == "新疆35选7":
        id = 1
    elif str == "江苏7位数":
        id = 2
    elif str == "黑龙江6+1":
        id = 3
    elif str == "华东15选5":
        id = 4
    elif str == "广西快乐双彩":
        id = 5
    elif str == "好彩1":
        id = 6
    elif str == "南粤36选7":
        id = 7
    elif str == "福建36选7":
        id = 8
    elif str == "福建22选5":
        id = 9
    elif str == "东方6+1":
        id = 10
    elif str == "双色球":
        id = 11
    elif str == "七星彩":
        id = 12
    elif str == "七乐彩":
        id = 13
    elif str == "排列5":
        id = 14
    elif str == "排列3":
        id = 15
    elif str == "福彩3D":
        id = 16
    return id












