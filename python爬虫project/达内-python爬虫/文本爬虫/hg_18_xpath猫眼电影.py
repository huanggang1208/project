# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_18_xpath猫眼电影.py
import random
import time
import requests
from lxml import etree


class XpathMaoyan:
    def __init__(self):
        self.url = "https://www.maoyan.com/films?showType=3&sortId=3&offset={}"
        self.headers = {
            "user-agent": "User-Agent,Mozilla/5.0"
        }
        self.i = 0

    def base_get_html(self, url):
        base_html = requests.get(url=url, headers=self.headers).text

        self.base_parse_html(base_html)

    def base_parse_html(self, html):
        p = etree.HTML(html)
        href_list = p.xpath('//div[@class="movies-list"]/dl[1]//a/@href')
        for href in href_list:
            detail_url = "https://www.maoyan.com" + href
            print(detail_url)
            resp = requests.get(url=detail_url, headers=self.headers, verify=False)
            resp.encoding = "utf-8"
            detail_html = resp.content
            time.sleep(random.uniform(0, 3))
            print(detail_html)

            self.detail_parse_html(detail_html)

    def detail_parse_html(self, html):
        p = etree.HTML(html)
        item = {}
        item["电影名字"] = p.xpath('//div[@class="banner"]//h1/text()')
        # item["类型"] = p.xpath('//div[@class="banner"]//ul/li[1]/text()')
        # item["地方"] = p.xpath('//div[@class="banner"]//ul/li[2]/text()')
        # item["上映时间"] = p.xpath('//div[@class="banner"]//ul/li[3]/text()')
        print(item)

    def run(self):
        i = int(input("页码："))
        url = self.url.format((i - 1) * 30)
        self.base_get_html(url)


if __name__ == '__main__':
    spider = XpathMaoyan()
    spider.run()
