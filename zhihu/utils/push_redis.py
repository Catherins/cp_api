from scrapy.utils.project import get_project_settings
import redis
import requests
from lxml import etree
from items import ZhihuItem
from items import ShishicaiItem
from items import GopinItem
from matchId import match_CrawlA
from matchId import matchid_Example
from matchId import matchid_Jngp
import datetime
import re

#redis
settings = get_project_settings()
r = redis.StrictRedis(host=settings['REDIS_HOST'],
                      port=settings['REDIS_PORT'],
                      password=settings['REDIS_PASSWORD'])

def push_redis(url,crawl_name):
    with open(url, 'r') as file:
        url_list = file.readlines()
        print(len(url_list))
        for eachone in url_list:
            r.lpush(crawl_name, eachone)
            print(eachone)



def get_redis_crawl(crawl_name):
    print(crawl_name)
    if crawl_name == 'crawlA':
        items = []
        while True:
            try:
                url = r.lpop('crawlA_url')
                try:
                    res = requests.get(url)
                    html = etree.HTML(res.content)
                    # 名字
                    name = html.xpath('//*[@id="jq_df_kc_gameName"]/text()')
                    # id
                    id = match_CrawlA(name[0])
                    # 期数
                    kaijiang_data = html.xpath('//*[@id="jq_body_kc_result"]/tr[1]/td[1]/text()')
                    print(kaijiang_data[0])
                    # 开奖时间
                    kaijiang_day = html.xpath('//*[@id="jq_body_kc_result"]/tr[1]/td[2]/text()')
                    # 中奖号码
                    numb = html.xpath('//*[@id="jq_body_kc_result"]/tr[1]/td[3]/text()')
                    a = numb[0]
                    b = a.replace("\r", "")
                    c = b.replace("\n", "")
                    d = c.replace("\t", "")
                    e = d.replace(" ", "")
                    f = e.replace("|", ",")
                    item = ShishicaiItem()
                    item['id'] = id
                    item['name'] = name[0]
                    item['kaijiang_data'] = kaijiang_data[0]
                    item['kaijiang_numb'] = f
                    item['kaijiang_day'] = kaijiang_day[0]
                    items.append(item)

                except Exception as e:
                    print(e)
                    break

            except Exception as e:
                print(e)
                break
        return items




    elif crawl_name == 'crawlC':
        while True:
            items = []
            try:
                url = r.lpop('crawlC_url')

                try:
                    response = requests.get(url)
                    html = etree.HTML(response.text)
                    # 名字
                    name = html.xpath('//a[@class="strong"]/text()')
                    id = matchid_Example(name[0])
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
                    items.append(item)
                except Exception as e:
                    print("error")
                    break
            except Exception as e:
                print(e)
                break
        return items
    elif crawl_name == 'crawlB':
        print('crawlB_url')
        while True:
            arr = []
            try:
                url = r.lpop('crawlB_url')
                print('crawlB_url')
                url = url.decode('utf-8')
                date_now = datetime.datetime.now().strftime('%Y-%m-%d')
                url = re.findall(r"(.+?).html", url)
                url = url[0] + '/' + date_now + '.html'
                try:
                    res = requests.get(url)
                    html = etree.HTML(res.content)
                    # 名字
                    name = html.xpath('/html/body/div[5]/a[4]/text()')
                    print(name[0])
                    # id
                    id = matchid_Jngp(name[0])
                    # 期号list
                    qihao_list = html.xpath('//div[@class="bd clearfix"]/table[1]/tr/td[1]/text()')
                    # 时间list
                    date_list = html.xpath('//div[@class="bd clearfix"]/table[1]/tr/td[2]/text()')
                    # 开奖号码list
                    kaijiang_list = html.xpath('//div[@class="bd clearfix"]/table[1]/tr/td[3]/text()')

                    for i in range(len(qihao_list)):
                        print(i)
                        item = GopinItem()
                        item['id'] = id
                        item['name'] = name[0]
                        item['qihao'] = qihao_list[i]
                        item['kaijiang_data'] = date_list[i]
                        item['kaijiang_numb'] = kaijiang_list[i]
                        item['kaijiang_day'] = date_now
                        arr.append(item)

                except Exception as e:
                    print(e)
                    break
            except Exception as e:
                print(e)
                break
        return arr