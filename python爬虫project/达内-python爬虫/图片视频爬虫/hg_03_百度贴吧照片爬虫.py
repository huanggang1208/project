# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_03_百度贴吧照片爬虫.py
"""//div[@class="t_con cleafix"]/div/div/div/a/@href"""
import random
import time

import requests
import os.path
from lxml import etree
"""//div[@class="d_post_content j_d_post_content  clearfix"]/img/@src | //div[@class="d_post_content j_d_post_content clearfix"]/img/@src"""


class BaiduSpider(object):
    def __init__(self):
        self.url = "https://tieba.baidu.com/f?ie=utf-8&kw={}&pn={}"
        self.headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"}

        self.proxy = {
            "http": "211.65.197.93:80",
            "https": "211.65.197.93:80"
        }
        self.i = 1

    def get_html(self, url):
        """功能函数一：获取html"""
        html = requests.get(url=url, headers=self.headers).text
        return html

    def xpath_func(self, html, xpath):
        """功能函数二：解析html"""
        p = etree.HTML(html)
        print(p)
        p_list = p.xpath(xpath)
        print(p_list)

        return p_list

    def parse_html(self, one_url):
        """获取一级页面，提取帖子链接"""
        one_html = self.get_html(url=one_url)

        one_xpath = '//div[@class="t_con cleafix"]/div/div/div/a/@href'
        href_list = self.xpath_func(html=one_html, xpath=one_xpath)
        for href in href_list:
            print(href)
            self.get_image(href)

    def get_image(self, href):
        two_url = "https://tieba.baidu.com" + href
        two_html = self.get_html(url=two_url)
        two_xpath = '//div[@class="d_post_content j_d_post_content  clearfix"]/img/@src | //div[' \
                    '@class="d_post_content j_d_post_content clearfix"]/img/@src '
        image_list = self.xpath_func(two_html, two_xpath)

        for image in image_list:
            image_html = requests.get(url=image, headers=self.headers).content
            filename = image[-10:]
            with open(filename, "wb") as f:
                f.write(image_html)

            self.i += 1

    def run(self):
        name = input("输入名字：")
        start = int(input("请输入起始页："))
        end = int(input("请输入终止页："))
        for i in range(start, end+1):
            pg = i * 50
            self.parse_html(self.url.format(name, pg))
        time.sleep(random.uniform(0, 2))


if __name__ == '__main__':
    spider = BaiduSpider()
    spider.run()






