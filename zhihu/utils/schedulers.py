from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from push_redis import get_redis_crawl


def job(crawl_name):
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    scheduler = BlockingScheduler()
    scheduler.add_job(get_redis_crawl(crawl_name), 'interval', seconds=3)
    try:
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        pass