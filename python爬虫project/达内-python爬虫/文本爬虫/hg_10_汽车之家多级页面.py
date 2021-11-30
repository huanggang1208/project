# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_10_汽车之家多级页面.py
import re
import time
import random
import csv
from urllib import request


class CarSpider:
    def __init__(self):
        self.url = "https://www.che168.com/beijing/a0_0msdgscncgpi1ltocsp2exx0/?pvareaid=102179#currengpostion"
        self.headers = {"user-agent": "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50"}

    def get_html(self, url):
        # 功能函数一：获取响应内容
        req = request.Request(url=url, headers=self.headers)
        res = request.urlopen(req)
        # 知识点一：ignore：decode（）时遇到不能识别的字符，则忽略掉
        # 二：decode（）时，如果出现乱码，则去查看网页的字符编码是什么
        html = res.read().decode("gb2312", "ignore")
        return html

    def re_func(self, regex, html):
        # 功能函数二：解析提取数据
        pattern = re.compile(regex, re.S)
        r_list = pattern.findall(html)
        return r_list

    def parse_html(self, one_url):
        # 数据抓取函数-从一级页面解析开始
        one_html = self.get_html(one_url)
        one_regex = '<li class="cards-li list-photo-li ".*?<a href="(.*?)" class="carinfo" target="_blank.*?</div>'
        # href_list:[]
        href_list = self.re_func(one_regex, one_html)
        href_list_real = []

        for href in href_list:
            if href[0] in "/":

                href_list_real.append(href)

        # 拼接汽车详情页
        for href_real in href_list_real:
            car_url = "https://www.che168.com" + href_real
            print(car_url)
            self.get_data(car_url)
            # 抓取一辆汽车控制频率
        time.sleep(random.uniform(1, 3))

    def get_data(self, car_url):
        # 抓取一辆汽车的详情数据
        two_html = self.get_html(car_url)
        two_regex = '<div class="car-box">.*?<h3 class="car-brand-name">(.*?)</h3>.*?<h4>(.*?)</h4>.*?<h4>(' \
                    '.*?)</h4>.*?</div> '
        car_list = self.re_func(two_regex, two_html)


        item = {}
        for i in car_list:
            item["name"] = i[0].strip()
            item["km"] = i[1].strip()
            item["time"] = i[2].strip()
            print(item)

    def run(self):
        # 程序入口函数，拼接函数

        url = self.url
        self.parse_html(url)


if __name__ == '__main__':
    spider = CarSpider()
    spider.run()
