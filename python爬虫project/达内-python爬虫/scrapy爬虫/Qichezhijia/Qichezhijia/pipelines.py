# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


# 管道一：打印输出
class QichezhijiaPipeline:
    def process_item(self, item, spider):
        print(item)

        return item


# 管道二：存入mysql
# 建库建表
"""
终端：
create database qichezhijiadb charset utf8
use qichezhijiadb
create table qichezhijia(
name varchar(200),
price varchar(100)
)charset=utf8
"""
# import pymysql
#
#
# class QichezhijiaMysqlPipeline(object):
#     def __init__(self):
#         self.db = pymysql.connect(host='localhost', user='root', password='941208', database='qichezhijiadb', charset='utf8')
#         self.cur = self.db.cursor()
#
#     def open_spider(self, spider):
#         """爬虫程序开始，只执行一次，一般用于数据库的连接"""
#         # 创建游标对象
#
#     def process_item(self, item, spider):
#         ins = 'insert into qichezhijatab values(%S,%s)'
#         li = [
#             item["name"].strip(),
#             item["price"].strip()
#         ]
#         self.cur.execute(ins, li)
#         # 提交到数据库执行
#         self.db.commit()
#         return item
#
#     def close_spider(self, spider):
#         """爬虫程序结束，开启一次"""
#         self.cur.close()
#         self.db.close()


# 创建管道三：存入mongodb
import pymongo
from .settings import *


class QichezhijiaMongoPipeline(object):
    def __init__(self):
        self.conn = pymongo.MongoClient(MONGO_HOST, MONGO_PORT)
        self.db = self.conn[MONGO_DB]
        self.myset = self.db[MONGO_SET]

    def open_mongo(self, spider):
        """lianjie db"""

    def process_item(self, item, spider):
        d = dict(item)
        self.myset.insert_one(d)

        return item
