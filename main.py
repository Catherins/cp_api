from scrapy import cmdline
from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

#cmdline.execute("scrapy crawl crawlA".split())




print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
scheduler = BlockingScheduler()
scheduler.add_job(cmdline.execute("scrapy crawl crawlA".split()), 'interval', seconds=3)
try:
    scheduler.start()
except Exception as e:
    print(e)
    pass






