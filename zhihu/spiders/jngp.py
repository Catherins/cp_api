#coding：utf-8
import scrapy
import requests
from bs4 import BeautifulSoup
import re
from scrapy.utils.project import get_project_settings
import redis
from lxml import etree
from items import ZhihuItem
from html.parser import HTMLParser
from lxml.html import fromstring, tostring
import datetime
import urllib
import chardet
#redis
settings = get_project_settings()
r = redis.StrictRedis(host=settings['REDIS_HOST'],
                      port=settings['REDIS_PORT'],
                      password=settings['REDIS_PASSWORD'])


class JngpSpider(scrapy.Spider):
    name = 'jngp'
    allowed_domains = ['www.8200.cn']
    start_urls = ['https://www.km28.com/lottery-gp/ahsyxw.html']

    def parse(self, response):
        this_machine = 'master1'
        print('开始分布式爬虫')
        if this_machine == 'master':
            link_list = []
            with open('D:\\python\\PycharmProjects\\zhihu\\jngp.txt', 'r') as file:
                url_list = file.readlines()
                for eachone in url_list:
                    link = re.findall('：(.*)', eachone)[0]
                    link_list.append(link)
                    r.lpush('url', link)
                    print(link)
                    if len(link_list) == 100:
                        break
        else:
            while True:
                try:
                    url = r.lpop('url')
                    url = url.decode('utf-8')
                    #print(type(url))
                    #https://www.km28.com/lottery-gp/ahsyxw/2020-09-19.html
                    date_now = datetime.datetime.now().strftime('%Y-%m-%d')
                    #print(date_now)
                    url = re.findall(r"(.+?).html",url)
                    url = url[0]+'/'+date_now+'.html'
                    #print(url)
                    try:
                        res = requests.get(url)
                        print(res.content)
                        html = etree.HTML(res.content)
                        # 转为string
                        # 名字
                        name = html.xpath('/html/body/div[5]/a[4]/text()')
                        #id
                        id = match_id(name[0])
                        #print(name)
                        # 期号/时间/开奖号码/html/body/div[6]/div[2]/div/table[1]/tbody/tr[1]/td[1]
                        qihao_list = html.xpath('/html/body/div[6]/div[2]/div/table[1]/tbody/tr[1]/td[1]')
                        if len(qihao_list) == 0:
                            print('没有值')

                        else:
                          for qihao in qihao_list:
                            qihao = qihao
                            print(qihao)

                        #/html/body/div[6]/div[2]/div/table[1]/tbody

                        # 开奖号码
                        #kaijiang_numb = html.xpath('/html/body/div[6]/div[2]/div/table[1]/tbody/tr[1]/td/text()')
                        # print(kaijiang_numb)
                        #item = ZhihuItem()
                        #item['id'] = id
                        #item['name'] = name[0]
                        #item['kaijiang_day'] = kaijiang_data[0]
                        #item['kaijiang_data'] = kaijiang_data[0]

                        # str = ''
                        #for i in kaijiang_numb:
                            #str += i
                        #print(str)
                        #item['kaijiang_numb'] = str
                        #yield item
                    except Exception as e:
                        print(e)
                        break
                except Exception as e:
                    print(e)
                    break


def match_id(str):
    id = 0
    if str == "安徽11选5":
        id = 1
    elif str == "福建11选5":
        id = 2
    elif str == "甘肃11选5":
        id = 3
    elif str == "广西11选5":
        id = 4
    elif str == "辽宁11选5":
        id = 5
    elif str == "内蒙古11选5":
        id = 6
    elif str == "陕西11选5":
        id = 7
    elif str == "天津11选5":
        id = 8
    elif str == "新疆11选5":
        id = 9
    elif str == "浙江11选5":
        id = 10
    elif str == "甘肃快三":
        id = 11
    elif str == "贵州快三":
        id = 12
    elif str == "吉林快三":
        id = 13
    elif str == "江苏快三":
        id = 14
    elif str == "重庆快乐十分":
        id = 15
    elif str == "黑龙江快乐十分":
        id = 16
    elif str == "湖南快乐十分":
        id = 14
    elif str == "云南快乐十分":
        id = 15
    elif str == "辽宁快乐十二":
        id = 16
    elif str == "四川快乐十二":
        id = 17
    elif str == "浙江快乐十二":
        id = 18
    elif str == "黑龙江时时彩":
        id = 19
    elif str == "内蒙古时时彩":
        id = 20
    elif str == "新疆时时彩":
        id = 21
    elif str == "云南时时彩":
        id = 22
    elif str == "上海时时乐":
        id = 23
    else:
        id = 0
    return id












