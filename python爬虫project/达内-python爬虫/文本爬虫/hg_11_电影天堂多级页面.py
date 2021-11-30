# @Author:hggg
# @File:hg_11_电影天堂多级页面.py
import re
import time
import random
import requests
import csv


class MovieSpider:
    def __init__(self):
        self.url = "https://www.dydytt.net/html/gndy/dyzz/list_23_{}.html"
        self.headers = {"user-agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, " \
                                      "like Gecko) Version/5.1 Safari/534.50 "}
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

    def parse_html(self, one_url):
        # 数据抓取，从一级页面开始
        one_regex = '</tr>.*?<a href="(.*?)" class=".*?</tr>'
        one_html = self.get_html(one_url)
        href_list = self.re_fun(one_regex, one_html)

        for href in href_list:
            movie_url = "https://www.dydytt.net" + href
            self.get_data(movie_url)

        time.sleep(random.uniform(1, 3))

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
            url = self.url.format(i)
            self.parse_html(url)
        print(self.all_movie_list)
        self.writer.writerows(self.all_movie_list)
        self.f.close()


if __name__ == '__main__':
    spider = MovieSpider()
    spider.run()
