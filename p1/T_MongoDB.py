# 导包
from pymongo import MongoClient


# 连接MongoDB数据库
class Test:
    def __init__(self):
        self.client = MongoClient(host='localhost', port=27017)
        print(self.client)

    def getDBs(self):
        self.client.list_database_names()
        for db in self.client.list_database_name():
            print(db)

    def creatColl(self):
        bigdata = self.client['bigdata']  # 创建数据库bigdata
        bigdata.craete_collection('student')  # 创建集合student

    def getColl(self):
        self.bigdata = self.client['bigdata']
        collections = self.bigdata.list_collections()
        for coll in collections:
            print(coll)

    def inserOne(self):
        self.bigdata = self.client['bigdata']
        comment = self.bigdata['student']
        newDoc = {"name": "张三", "age": 19, "score": [80, 78, 85]}
        comment.insert_one(newDoc)

    def findDoc(self):
        self.bigdata = self.client['bigdata']
        comment = self.bigdata['student']
        documents = comment.find()
        for document in documents:
            print(document)

    def updataDoc(self):
        self.bigdata = self.client['bigdata']
        comment = self.bigdata['student']
        comment.update_one({"name": "张三"}, {"set": {"age": 20}})

    def deletDoc(self):
        self.bigdata = self.client['bigdata']
        comment = self.bigdata['student']
        comment.delete_one({"name": "张三"})

    def dropColl(self):
        bigdata = self.client['bigdata']
        bigdata.drop_collection('student')


if __name__ == '__main__':
    test = Test()
    test.deletDoc()
