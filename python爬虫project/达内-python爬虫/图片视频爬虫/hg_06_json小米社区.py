# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_06_json小米社区.py
import json
from jsonpath import jsonpath
import requests
import time
import random
from fake_useragent import UserAgent
import os.path


class Xiaomi:
    def __init__(self):
        self.url = "https://prod.api.xiaomi.cn/community/square?start={}&limit=10"
        self.i = 0

    def get_html(self, url):
        headers = {"user-agent": UserAgent().random}
        html = requests.get(url=url, headers=headers).json()

        self.parse_html(html)

    def parse_html(self, html):
        item = {}
        pic_url_list = []
        # for record_list in jsonpath(html, "$..entity"):
        #     # print(record_list)
        #     print(type(record_list))
        records = html["entity"]["records"]
        # print(records)
        for record in records:
            if "pic" in record:
                item["id"] = record["id"]
                item["userid"] = record["userId"]
                item["type"] = record["type"]
                item["title"] = record["title"]
                item["picUrl"] = record["pic"]

                pic_url_list.append(item["picUrl"])
        print(pic_url_list)
        for pic_url in pic_url_list:
            self.get_pic_html(pic_url)

    def get_pic_html(self, url):
        self.i += 1
        headers = {"user-agent": UserAgent().random}
        pic_html = requests.get(url=url, headers=headers).content
        filename = "E:/pycharm/project/python爬虫project/达内-python爬虫/图片视频爬虫/images/"\
                   + str(self.i) + ".jpg"
        with open(filename, "wb") as f:
            f.write(pic_html)

    def run(self):
        for pn in range(1, 10):

            page = (pn - 1) * 9
            self.get_html(self.url.format(page))
            time.sleep(random.randint(0, 2))
        print("抓取{}张".format(self.i))


if __name__ == '__main__':
    spider = Xiaomi()
    spider.run()

