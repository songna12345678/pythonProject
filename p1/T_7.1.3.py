import pymongo
client = pymongo.MongoClient('localhost',27017)#连接数据库
mydb = client['mydb']
test = mydb['test']

