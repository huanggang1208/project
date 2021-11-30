# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_20_xpath链家.py
import random
import time
import redis
import sys
from hashlib import md5
import csv
import requests
from lxml import etree
from fake_useragent import UserAgent
import pandas as pd


class LianjiaSpider:
    def __init__(self):
        self.url = "https://bj.lianjia.com/ershoufang/pg{}/"
        self.r = redis.Redis(host="localhost", port=6379, db=0)
        self.headers = ['address', 'area', 'total', 'model', 'type', 'name', 'perfect', 'direct', 'year', 'floor']
        self.f = open("链家房源.csv", "a", newline="", encoding='utf-8-sig')
        # 提前预览列名，当下面代码写入数据时，会将其一一对应。
        self.writer = csv.DictWriter(self.f, fieldnames=self.headers)
        self.writer.writeheader()  # 写入列名

        self.all_house_list = []

    def get_html(self, url):
        headers = {"user-agent": UserAgent().random}
        for i in range(3):
            html = requests.get(url=url, headers=headers, timeout=2).text
            self.parse_html(html)

    def md5_li(self, li):
        # 对URL地址进行md5的加密，生成请求指纹
        s = md5()
        s.update(str(li).encode("utf-8"))

        return s.hexdigest()

    def parse_html(self, html):
        p = etree.HTML(html)
        li_list = p.xpath('//li[@class="clear LOGVIEWDATA LOGCLICKDATA"]')
        for li in li_list:
            # 抓取之前进行判断
            finger = self.md5_li(li)
            if self.r.sadd("Lianjia_spider:fingers", finger) == 1:
                self.get_data(li)
                # 随机休眠
                time.sleep(random.uniform(0, 1))
            else:
                sys.exit("抓取完成")

    def get_data(self, li):
        item = {}
        name_list = li.xpath('.//div[@class="positionInfo"]/a[1]/text()')
        item["name"] = name_list[0].strip() if name_list else None
        address_list = li.xpath('.//div[@class="positionInfo"]/a[2]/text()')
        item["address"] = address_list[0].strip() if address_list else None
        info_list = li.xpath('.//div[@class="houseInfo"]/text()')
        if info_list:
            info_list = info_list[0].split('|')
            if len(info_list) == 7:
                item["model"] = info_list[0].strip()
                item["area"] = info_list[1].strip()
                item["direct"] = info_list[2].strip()
                item["perfect"] = info_list[3].strip()
                item["floor"] = info_list[4].strip()
                item["year"] = info_list[5].strip()
                item["type"] = info_list[6].strip()
            else:
                item["model"] = item["area"] = item["direct"] = item["perfect"] = item["floor"] = item["year"] = item[
                    "type"] = None
        total_list = li.xpath('.//div[@class="totalPrice totalPrice2"]/span/text()')
        item["total"] = total_list[0].strip() if total_list else None

        self.writer.writerow(item)  # 写入数据

        print(item)

    def run(self):
        pg = input("输入页数：")
        url = self.url.format(pg)
        self.get_html(url)
        time.sleep(random.uniform(1, 2))


if __name__ == '__main__':
    spider = LianjiaSpider()
    spider.run()
