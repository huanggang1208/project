# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_02_多张照片爬虫.py
import os.path
import random
import re
import time
from urllib import parse
import requests


class ImageSpider:
    def __init__(self):

        self.url = "https://image.baidu.com/search/index?tn=baiduimage&word={}"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) "
                          "Chrome/14.0.835.163 Safari/535.1"
        }
        self.name = input("输入名字：")
        self.directory = "./my_images/{}/".format(self.name)
        self.i = 1
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def parse_html(self):
        # params = parse.quote(self.name)
        resp = requests.get(url=self.url.format(self.name), headers=self.headers)
        resp.encoding = "utf-8"
        print(resp.status_code)
        html = resp.text
        print(html)
        regex = 'thumbURL":"(.*?)"'
        pattern = re.compile(regex, re.S)
        src_list = pattern.findall(html)
        print(src_list)
        for src in src_list:
            print(src)
            # 保存一张图片到本地
            self.save_image(src)

    def save_image(self, src):
        html = requests.get(url=src, headers=self.headers).content
        filename = self.directory + "({}_{}).jpg".format(self.name, self.i)
        with open(filename, "wb") as f:
            f.write(html)
        print(filename, "保存成功")
        self.i += 1

    def run(self):
        self.parse_html()
        time.sleep(random.uniform(1, 2))


if __name__ == '__main__':
    spider = ImageSpider()
    spider.run()
