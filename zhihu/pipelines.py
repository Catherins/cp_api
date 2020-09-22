import pymongo
from scrapy.utils.project import get_project_settings
from items import ZhihuItem
from items import GopinItem

class ZhihuPipeline:
    def __init__(self):
        settings = get_project_settings()



    def process_item(self,item,spider):
        settings = get_project_settings()
        if isinstance(item,GopinItem):
            doc_name = settings['MONGODB_DOCNAME']
        elif isinstance(item,ZhihuItem):
            doc_name = settings['MONGODB_DOCNAME_GP']
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        db_name = settings['MONGODB_DBNAME']
        client = pymongo.MongoClient(host=host, port=port)
        db = client[db_name]
        self.post = db[doc_name]
        print(client)
        self.post.insert(dict(item))
        return item