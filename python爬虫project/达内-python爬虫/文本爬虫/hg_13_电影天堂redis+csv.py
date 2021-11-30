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
        self.f = open("电影天堂.csv", "a", newline="", encoding='utf-8-sig')
        self.writer = csv.writer(self.f)
        self.all_movie_list = []

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
        one_regex = '<b>.*?<a href="(.*?)" class=".*?</b>'
        one_html = self.get_html(one_url)
        href_list = self.re_fun(one_regex, one_html)

        for href in href_list:
            # 拼接详情页url
            movie_url = "https://www.dydytt.net" + href

            # 抓取之前进行判断
            finger = self.md5_url(movie_url)
            if self.r.sadd("movie_spider:fingers", finger) == 1:
                self.get_data(movie_url)
                # 随机休眠
                time.sleep(random.uniform(0, 1))
            else:
                sys.exit("抓取完成")

    def get_data(self, movie_url):
        # 抓取每一部电影的信息
        two_regex = '<tr>.*?<br />◎译　　名　(.*?)<br />◎片　　名　(.*?)<br />◎年　　代　(.*?)' \
                    '<br />◎产　　地　(.*?)<br />◎类　　别　(.*?)<br />◎语　　言.*?<br />◎豆瓣评分　(.*?) from .*?<tr>'
        two_html = self.get_html(movie_url)
        movie_list = self.re_fun(two_regex, two_html)

        for m in movie_list:
            movie_t = (
                m[0].strip(),
                m[1].strip(),
                m[2].strip(),
                m[3].strip(),
                m[4].strip(),
                m[5].strip(),
            )
            print(movie_t)
            self.all_movie_list.append(movie_t)

    def run(self):
        for i in range(1, 3):
            print(i)

            url = self.url.format(i)
            self.parse_html(url)

        self.writer.writerows(self.all_movie_list)
        
        self.f.close()


if __name__ == '__main__':
    spider = MovieSpider()
    spider.run()

