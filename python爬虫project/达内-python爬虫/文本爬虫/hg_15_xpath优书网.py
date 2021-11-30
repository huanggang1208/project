# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_15_xpath优书网.py
import requests
from lxml import etree


class Spider1688:
    def __init__(self):
        self.url = "https://www.yousuu.com/rank/readIndex?page={}"
        self.headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, "
                                      "like Gecko) Chrome/94.0.4606.61 Safari/537.36"}
        self.i = 0

    def get_html(self, url):
        html = requests.get(url=url, headers=self.headers).text

        self.base_parse_html(html)

    def base_parse_html(self, html):
        p = etree.HTML(html)
        href_list = p.xpath('//*[@id="app"]//div[@class="result-item-layout full-mode-book"]/div[1]/div[1]/div['
                            '1]/a/@href')
        for href in href_list:
            global book_url
            book_url = "https://www.yousuu.com" + href
            print(book_url)
            resp = requests.get(url=book_url, headers=self.headers)
            resp.encoding = "utf-8"
            book_html = resp.text
            self.i += 1
            self.detail_parse_html(book_html)

    def detail_parse_html(self, html):
        p = etree.HTML(html)
        item = {}
        item["url"] = book_url
        item["name"] = p.xpath('.//div[@class="book-info"]/h1/text()')[0]
        item["writer"] = p.xpath('.//div[@class="book-info-detail"]/p/a/text()')[0]
        item["score"] = p.xpath('.////*[@id="app"]/div[2]/section/div/header/div/div[2]/div/div[1]/div[1]/p[1]/text()')[0]
        print(item)

    def run(self):
        page = input("输入页数：")
        self.get_html(self.url.format(page))
        print(self.i)


if __name__ == '__main__':
    spider = Spider1688()
    spider.run()
