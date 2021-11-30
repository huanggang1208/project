# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_25_豆瓣全站爬取.py
import json
import random
import re
import time
import requests
from fake_useragent import UserAgent


class DoubanSpiderAll:
    def __init__(self):
        self.url = "https://movie.douban.com/j/chart/top_list?type={}" \
                   "&interval_id=100%3A90&action=&start={}&limit=20"
        self.i = 0
        self.data = {'Cookie': 'douban-fav-remind=1; __gads=ID=3d542780802e38f5-225582d882c400dc:T=1604215881:RT'
                               '=1604215881:S=ALNI_Mb_5JdjCjL5i-IIMIo4QRmm2rp7EA; ll="108288"; bid=NVMM84_OZN4; '
                               '_vwo_uuid_v2=DA4FB0B92BE1BAB34414418E5B5CF9FF1|302202f6bed70244a65b06cd7380ddab; '
                               'viewed="35292992"; gr_user_id=94d2b785-575b-4ebe-9b3a-9a5f7b9b35ee; '
                               '__yadk_uid=DZRzoUbQqLqMEnoOZgpIHuYdVMbXKtNl; dbcl2="209042263:GdqZyAUX5xE"; '
                               'push_noty_num=0; push_doumail_num=0; '
                               '__utmz=30149280.1637498093.17.6.utmcsr=open.weixin.qq.com|utmccn=('
                               'referral)|utmcmd=referral|utmcct=/; ck=462L; '
                               '_pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1637542896%2C%22https%3A%2F%2Fwww.baidu.com'
                               '%2Fs%3Fie%3DUTF-8%26wd%3D%25E8%25B1%2586%25E7%2593%25A3%22%5D; _pk_ses.100001.4cf6=*; '
                               '__utma=30149280.1279800892.1556521961.1637498093.1637542896.18; '
                               '__utmb=30149280.0.10.1637542896; __utmc=30149280; '
                               '__utma=223695111.1596328959.1556521961.1637498093.1637542896.14; '
                               '__utmb=223695111.0.10.1637542896; __utmc=223695111; '
                               '__utmz=223695111.1637542896.14.8.utmcsr=baidu|utmccn=('
                               'organic)|utmcmd=organic|utmctr=%E8%B1%86%E7%93%A3; '
                               '_pk_id.100001.4cf6=00b9b32232f9e06c.1556521961.14.1637542901.1637498093.'}
        # self.proxy = {
        #     'http': 'http:58.152.94.165:8080',
        #     'https': 'https:58.152.94.165:8080'
        # }

    def get_html(self, url):
        headers = {"user-agent": UserAgent().random}
        html = requests.get(url=url, data=self.data, headers=headers).text

        return html

    def parse_html(self, url):
        html = json.loads(self.get_html(url))
        item = {}
        for one_film in html:
            item["name"] = one_film["title"]
            item["types"] = one_film["types"]
            item["score"] = one_film["score"]
            item["rank"] = one_film["rank"]
            item["url"] = one_film["url"]
            self.i += 1

            print(item)

    def run(self):
        # type_dic:{“剧情”：“21”，“爱情”：“23”，“喜剧”：“32”}
        type_dic = self.get_type_dic()
        print(type_dic)
        menu = ""
        for t in type_dic:
            menu = menu + t + '|'
        print(menu)
        type_choice = input("输入要抓取的类别：")
        # typ：类型就是输入类型对应的字典的value
        typ = type_dic[type_choice]
        # total：电影的总数量
        total = self.get_total()
        for page in range(0, total, 20):
            self.parse_html(self.url.format(typ, page))
            time.sleep(random.uniform(1, 3))
        print("抓取%d部电影" % self.i)

    def get_type_dic(self):
        url = "https://movie.douban.com/chart"
        html = self.get_html(url)
        print(html)
        regex = '<span><a href=".*?type_name=(.*?)&type=(.*?)&.*?</span>'
        pattern = re.compile(regex, re.S)
        r_list = pattern.findall(html)
        # r_list:[("剧情","31"),("喜剧","2"),("爱情","12")]
        type_dic = {}
        for r in r_list:
            type_dic[r[0]] = r[1]

        return type_dic

    def get_total(self):
        url = "https://movie.douban.com/j/chart/top_list_count?type=11&interval_id=100%3A90"
        html = json.loads(self.get_html(url=url))
        total = html["total"]

        return total


if __name__ == '__main__':
    spider = DoubanSpiderAll()
    spider.run()





