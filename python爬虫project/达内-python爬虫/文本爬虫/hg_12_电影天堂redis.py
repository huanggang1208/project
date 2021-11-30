# @Author:hggg
# @File:hg_11_电影天堂多级页面.py
import re
import time
import random
import requests
import redis
import sys
from hashlib import md5
import csv


class MovieSpider:
    def __init__(self):
        self.url = "https://www.dydytt.net/html/gndy/dyzz/list_23_{}.html"
        self.headers = {"user-agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, " \
                                      "like Gecko) Version/5.1 Safari/534.50 "}
        self.r = redis.Redis(host="localhost", port=6379, db=0)

    def get_html(self, url):
        resp = requests.get(url=url, headers=self.headers)
        resp.encoding = "gb2312"
        html = resp.text

        return html

    def re_fun(self, regex, html):
        # 解析提取数据
        pattern = re.compile(regex, re.S)
        r_list = pattern.findall(html)

        return r_list

    def md5_url(self, url):
        # 对URL地址进行md5的加密，生成请求指纹
        s = md5()
        s.update(url.encode())

        return s.hexdigest()

    def parse_html(self, one_url):
        # 数据抓取，从一级页面开始
        one_regex = '</tr>.*?<a href="(.*?)" class=".*?</tr>'
        one_html = self.get_html(one_url)
        href_list = self.re_fun(one_regex, one_html)

        for href in href_list:
            # 拼接详情页url
            movie_url = "https://www.dydytt.net" + href

            # 抓取之前进行判断
            finger = self.md5_url(movie_url)
            if self.r.sadd("moviespider:fingers", finger) == 1:
                self.get_data(movie_url)
                # 随机休眠
                time.sleep(random.uniform(1, 3))
            else:
                sys.exit("抓取完成")

    def get_data(self, movie_url):
        # 抓取每一部电影的信息
        two_regex = '<tr>.*?<br />◎译　　名　(.*?)<br />◎片　　名　(.*?)<br />◎年　　代　(.*?)' \
                    '<br />◎产　　地　(.*?)<br />◎类　　别　(.*?)<br />◎语　　言.*?<br />◎豆瓣评分　(.*?) from .*?<tr>'
        two_html = self.get_html(movie_url)
        movie_list = self.re_fun(two_regex, two_html)
        item = {}
        for m in movie_list:
            item["tran_name"] = m[0].strip()
            item["name"] = m[1].strip()
            item["year"] = m[2].strip()
            item["place"] = m[3].strip()
            item["type"] = m[4].strip()
            item["score"] = m[5].strip()

            print(item)

    def run(self):
        for i in range(1, 3):
            url = self.url.format(i)
            self.parse_html(url)


if __name__ == '__main__':
    spider = MovieSpider()
    spider.run()
    spider.resp.close()
