import pymongo
from scrapy.utils.project import get_project_settings
from items import ZhihuItem
from items import GopinItem

<<<<<<< HEAD
class crawlCPipeline:
    def __init__(self):
        print('境内低频')
        settings = get_project_settings()
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        db_name = settings['MONGODB_DBNAME']
        doc_name = settings['MONGODB_DOCNAME']
        client = pymongo.MongoClient(host=host, port=port)
        print(client)
        db = client[db_name]
        self.post = db[doc_name]

    def process_item(self,item,spider):
        self.post.insert(dict(item))
        return item


class crawlBGaopinPipeline:
    def __init__(self):
        print('境内高频')
        settings = get_project_settings()
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        db_name = settings['MONGODB_DBNAME']
        doc_name = settings['MONGODB_DOCNAME_GP']
        client = pymongo.MongoClient(host=host, port=port)
        print(client)
        db = client[db_name]
        self.post = db[doc_name]

    def process_item(self,item,spider):
        self.post.insert(dict(item))
        return item

class crawlAPipeline:
    def __init__(self):
        print('时时彩')
        settings = get_project_settings()
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        db_name = settings['MONGODB_DBNAME']
        doc_name = settings['MONGODB_DOCNAME_SSC']
        client = pymongo.MongoClient(host=host, port=port)
        print(client)
        db = client[db_name]
        self.post = db[doc_name]

    def process_item(self,item,spider):
=======
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
>>>>>>> 73e3b0861c975ca93b49d03bd30ff277d362e20b
        self.post.insert(dict(item))
        return item