# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_novel.py
import requests
from lxml import etree
import os
import time
import random


class Novel:
    def __init__(self):
        self.url = 'http://seputu.com/'
        self.headers = {"user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                                      'like Gecko) Chrome/96.0.4664.45 '
                                      'Safari/537.36 '}
        self.i = 0
        # self.item = {}
        # self.big_item = {}
        # self.little_item = {}

    def get_html(self):
        html = requests.get(url=self.url, headers=self.headers).text

        self.parse_html(html)

    def parse_html(self, html):
        p = etree.HTML(html)
        parent_title_list = p.xpath('//div[@class="mulu-title"]/center/h2')

        global big_item, little_item, filename
        big_item = {}
        for parent_title in parent_title_list:
            big_item["parent_title"] = parent_title.xpath('./text()')[0].strip()
            directory = './novel/{}/'.format(big_item["parent_title"])
            if not os.path.exists(directory):
                os.mkdir(directory)

            print(big_item)

        son_title_list = p.xpath('//div[@class="box"]/ul/li/a')
        little_item = {}
        for son_title in son_title_list:
            little_item["son_title"] = son_title.xpath('./text()')[0]
            print(little_item)
            filename = './novel/{}/{}.txt'.format(
                big_item["parent_title"].replace(':', '_'),
                little_item["son_title"].replace(' ', '_')
            )

        novel_href_list = p.xpath('.//div[@class="box"]/ul/li/a')
        for novel_href in novel_href_list:
            novel_href = novel_href.xpath('./@href')[0]
            print(novel_href)
            self.get_novel(novel_href)
            time.sleep(random.uniform(0, 1))
            self.i += 1

    def get_novel(self, url):
        req = requests.get(url=url, headers=self.headers)
        req.encoding = 'utf-8'
        html = req.text
        p = etree.HTML(html)

        novel_item = {}
        novel_list = p.xpath('//div[@class="content-body"]/p/text()')
        novel_item["novel_content"] = '\n'.join(novel_list)
        # print(novel_item)

        with open(filename, "w", encoding='utf-8') as f:
            f.write(novel_item['novel_content'])
        print("{}{}完成".format(big_item["parent_title"].replace(':', '_'),
                              little_item["son_title"].replace(' ', '_')
                              ))

    def run(self):
        self.get_html()
        print("完成")


if __name__ == '__main__':
    spider = Novel()
    spider.run()
