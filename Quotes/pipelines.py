import pymongo
class QuotesPipeline(object):

    def __init__(self):
        self.conn = pymongo.MongoClient(
            'localhost',
            27017
        )

        db = self.conn['myQuotes']
        self.collection=db['Quotes_tb']

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
