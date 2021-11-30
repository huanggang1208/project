# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_17_xpath汽车之家.py
import random
import time

import requests
from lxml import etree


class CarXpath:
    def __init__(self):
        self.url = "https://www.che168.com/guiyang/a0_0msdgscncgpi1ltocsp{}exx0/?pvareaid=102179"
        self.headers = {
            "user-agent": "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"
        }
        self.i = 0

    def get_base_html(self, url):
        base_html = requests.get(url=url, headers=self.headers).text

        self.base_parse_html(base_html)

    def base_parse_html(self, html):
        p = etree.HTML(html)
        href_list = p.xpath('.//li[@name="lazyloadcpc"]/a/@href')
        for href in href_list:
            global detail_url
            detail_url = "https://www.che168.com" + href

            detail_html = requests.get(url=detail_url, headers=self.headers).text
            time.sleep(random.uniform(0, 3))
            self.i += 1

            self.detail_parse_html(detail_html)

    def detail_parse_html(self, html):

        p = etree.HTML(html)
        item = {}
        item["url"] = detail_url
        item["name"] = p.xpath('//input[@id="car_carname"]/@value')
        item["价格"] = p.xpath('//div[@class="goodstartmoney"]/text()')
        print(item)

    def run(self):
        i = input("?:")
        url = self.url.format(i)
        self.get_base_html(url)
        print("抓取%d" % self.i)


if __name__ == '__main__':
    spider = CarXpath()
    spider.run()
