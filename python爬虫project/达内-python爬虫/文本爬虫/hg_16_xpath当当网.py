# -*- coding = utf8 -*-
# @Author:hggg
import random
import time
import requests
from lxml import etree


class SpiderDang:
    def __init__(self):
        self.url = "http://bang.dangdang.com/books/fivestars/01.03.00.00.00.00-recent30-0-0-1-{}"
        self.headers = {
            "user-agent": "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"
        }
        self.i = 0

    def get_html(self, url):
        html = requests.get(url=url, headers=self.headers).text

        self.base_parse_html(html)

    def base_parse_html(self, html):
        p = etree.HTML(html)
        href_list = p.xpath('//ul[@class="bang_list clearfix bang_list_mode"]//div[@class="name"]/a/@href')
        for href in href_list:
            global book_url
            book_url = href
            print(book_url)
            resp = requests.get(url=book_url, headers=self.headers)
            resp.encoding = "gb2312"
            book_html = resp.text
            self.i += 1
            time.sleep(random.uniform(0, 3))
            self.detail_parse_html(book_html)

    def detail_parse_html(self, html):
        p = etree.HTML(html)
        item = {}
        item["链接"] = book_url
        item["书名"] = p.xpath('.//*[@id="product_info"]/div[1]/h1/@title')[0]
        item["作者"] = p.xpath('.//*[@id="author"]/a[1]/text()')[0]
        item["评价"] = p.xpath('.//div[@class="clearfix comment_tabs_wrap"]/span[2]/text()')[0]
        item["出版时间"] = p.xpath('.//*[@id="product_info"]/div[2]/span[3]/text()')[0].strip()
        print(item)

    def run(self):
        page = input("输入页数：")
        self.get_html(self.url.format(page))
        print(self.i)


if __name__ == '__main__':
    spider = SpiderDang()
    spider.run()

