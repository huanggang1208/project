# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_04_百度贴吧.py
from urllib import request
from urllib import parse
import time
import random


class BaiDuTieBa:

    def __init__(self):
        # 定义初始函数
        self.url = "https://tieba.baidu.com/f?kw={}&pn={}"
        self.headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, "
                          "like Gecko) Version/5.1 Safari/534.50"}

    def get_html(self, url):
        # 获取响应内容的函数
        req = request.Request(url=url, headers=self.headers)
        res = request.urlopen(req)
        html = res.read().decode()

        return html

    def parse_html(self):
        # 解析提取数据的函数
        pass

    def save_html(self, file_name, html):
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(html)

    def run(self):
        # 程序入口
        name = input("请输入要查看的名字：")
        start = int(input("请输入起始页："))
        end = int(input("请输入终止页："))
        params = parse.quote(name)
        # 拼接URL地址
        for page in range(start, end+1):
            pn = (page - 1) * 50
            url = self.url.format(params, pn)
            # 发请求，解析，保存
            html = self.get_html(url)
            file_name = "{}_第{}页.html".format(name, page)
            self.save_html(file_name, html)
            time.sleep(random.randint(0, 1))


if __name__ == '__main__':
    spider = BaiDuTieBa()
    spider.run()

