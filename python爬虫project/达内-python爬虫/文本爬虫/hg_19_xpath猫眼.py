# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_19_xpath猫眼.py
import random
import time
import requests
from lxml import etree


class XpathMaoyan:
    def __init__(self):
        self.url = "https://www.maoyan.com/board/4?offset={}&requestCode=7f62596cccc05e3330e79ad1b3b15c729bjta"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                          "like Gecko) Chrome/94.0.4606.61 Safari/537.36"
        }
        self.i = 0

    def get_html(self, url):
        html = requests.get(url=url, headers=self.headers).text

        self.parse_html(html)

    def parse_html(self, html):
        p = etree.HTML(html)
        item = {}
        dd_list = p.xpath('//dl[@class="board-wrapper"]/dd')
        for dd in dd_list:
            item["name"] = dd.xpath('.//p[@class="name"]/a/@title')[0].strip()
            item["star"] = dd.xpath('.//p[@class="star"]/text()')[0].strip()
            item["time"] = dd.xpath('.//p[@class="releasetime"]/text()')[0].strip()
            item["url"] = dd.xpath('.//p[@class="name"]/a/@href')[0].strip()
            print(item)

    def run(self):
        for i in range(0, 91, 10):
            url = self.url.format(i)
            self.get_html(url)
            time.sleep(random.uniform(0, 2))


if __name__ == '__main__':
    spider = XpathMaoyan()
    spider.run()
