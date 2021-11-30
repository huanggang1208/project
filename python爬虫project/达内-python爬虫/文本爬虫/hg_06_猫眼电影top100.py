# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_06_猫眼电影top100.py
import random
import re
import time
from urllib import request

"""<p class=.*?title="(.*?)" data-act.*?<p class=.*?(。*？）</p>.*?上映时间：(.*?)</p>"""


class MaoyanSpider:

    def __init__(self):
        self.url = "https://www.maoyan.com/board/4?offset={}"
        self.headers = {"user-agent": "Mozilla/5.0"}

    def get_html(self, url):
        req = request.Request(url=url, headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode()

        # 直接调用解析函数
        self.parse_html(html)

    def parse_html(self, html):
        """解析函数"""
        regex = '<p class=.*?title="(.*?)" class=.*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>'
        pattern = re.compile(regex, re.S)
        r_list = pattern.findall(html)
        # 直接调用数据处理函数
        self.save_html(r_list)

    def save_html(self, r_list):
        """数据处理函数"""
        item = {}
        for r in r_list:
            item["name"] = r[0].strip()
            item["star"] = r[1].strip()
            item["time"] = r[2].strip()
            print(item)

    def run(self):
        """程序入口函数"""
        for offset in range(0, 91, 10):
            url = self.url.format(offset)
            self.get_html(url)
            # 控制抓取频率
            time.sleep(random.randint(1, 2))


if __name__ == '__main__':
    spider = MaoyanSpider()
    spider.run()
