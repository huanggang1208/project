# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_05_虎扑壁纸.py
import random
import time

import requests
from lxml import etree


class HupuSpider(object):
    def __init__(self):
        self.url = "https://bbs.hupu.com/search?q=%E5%A3%81%E7%BA%B8&topicId=&sortby=general&page={}"
        self.headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"}
        # self.proxy = {
        #     "http": "115.223.7.61:80",
        #     "https": "115.223.7.61:80"
        # }

    def get_html(self, url):
        html = requests.get(url=url, headers=self.headers).text

        return html

    def func_xpath(self, html, xpath_object):
        p = etree.HTML(html)
        p_list = p.xpath(xpath_object)

        return p_list

    def parse_html(self, one_url):
        one_html = self.get_html(one_url)
        one_xpath = '//div[@class="content-outline"]/div/a[1]/@href'
        href_list = self.func_xpath(one_html, one_xpath)

        for href in href_list:
            self.get_image_url(href)
            time.sleep(random.uniform(0, 2))

    def get_image_url(self, href):
        two_html = self.get_html(href)
        two_xpath = '//div[@class="slate-image"]/p/img/@src'
        src_list = self.func_xpath(two_html, two_xpath)

        for src in src_list:
            print(src)
            src_html = requests.get(url=src, headers=self.headers).content
            filename = "E:/pycharm/project/python爬虫project/达内-python爬虫/图片视频爬虫/images/" + src[55:65] + ".jpg"
            with open(filename, "wb") as f:
                f.write(src_html)

    def run(self):
        pg = input("输入要爬取的页数：")
        self.parse_html(self.url.format(pg))


if __name__ == '__main__':
    spider = HupuSpider()
    spider.run()
