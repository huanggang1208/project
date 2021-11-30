# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_14_xpath爬亚马逊.py
import requests
import time
import random
from lxml import etree


class AmazonSpider:
    def __init__(self):
        self.url = "https://www.amazon.cn/s?i=specialty-aps&srs=2338777071&s=relevanceblender&page={}"
        self.headers = {"user-agent": "https://api2.firefoxchina.cn/home/chome_feed_rec.json?v=20211116160012"}
        self.i = 0

    def get_html(self, url):
        resp = requests.get(url=url, headers=self.headers)
        resp.encoding = "utf-8"
        html = resp.text

        self.base_parse_html(html)

    def base_parse_html(self, html):
        # 基准xpath
        p = etree.HTML(html)
        div_list = p.xpath('//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-2"]//a/@href')
        for href in div_list:
            detail_url = "https://www.amazon.cn" + href
            detail_html = requests.get(url=detail_url, headers=self.headers).text
            time.sleep(random.uniform(0, 2))
            self.detail_parse_html(detail_html)
            self.i += 1

    def detail_parse_html(self, html):
        p = etree.HTML(html)

        item = {}
        item["name"] = p.xpath('.//*[@id="productTitle"]/text()')[0].strip()
        item["price"] = p.xpath('.//div[@id="apex_desktop"]//span[@class="a-offscreen"]/text()')[0].strip()

        print(item)

    def run(self):
        i = input("输入要爬取的页数：")
        url = self.url.format(i)
        self.get_html(url)
        print("抓取%d件商品" % self.i)


if __name__ == '__main__':
    spider = AmazonSpider()
    spider.run()
