# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_20_xpath链家.py
import random
import time

import requests
from lxml import etree
from fake_useragent import UserAgent


class LianjiaSpider:
    def __init__(self):
        self.url = "https://bj.lianjia.com/ershoufang/pg{}/"

    def get_html(self, url):
        headers = {"user-agent": UserAgent().random}
        for i in range(3):
            try:
                html = requests.get(url=url, headers=headers, timeout=2).text
                self.parse_html(html)
            except Exception as e:
                print("try again...")

    def parse_html(self, html):
        p = etree.HTML(html)
        item = {}
        li_list = p.xpath('//li[@class="clear LOGVIEWDATA LOGCLICKDATA"]')
        for li in li_list:
            name_list = li.xpath('.//div[@class="positionInfo"]/a[1]/text()')
            item["name"] = name_list[0].strip() if name_list else None
            address_list = li.xpath('.//div[@class="positionInfo"]/a[2]/text()')
            item["address"] = address_list[0].strip() if address_list else None
            info_list = li.xpath('.//div[@class="houseInfo"]/text()')
            if info_list:
                info_list = info_list[0].split('|')
                if len(info_list) == 7:
                    item["model"] = info_list[0].strip()
                    item["area"] = info_list[1].strip()
                    item["direct"] = info_list[2].strip()
                    item["perfect"] = info_list[3].strip()
                    item["floor"] = info_list[4].strip()
                    item["year"] = info_list[5].strip()
                    item["type"] = info_list[6].strip()
                else:
                    item["model"] = item["area"] = item["direct"] = item["perfect"] = item["floor"] = item["year"] = item[
                        "type"] = None
            total_list = li.xpath('.//div[@class="totalPrice totalPrice2"]/span/text()')
            item["total"] = total_list[0].strip() if total_list else None

            print(item)

    def run(self):
        for pg in range(1, 101):
            url = self.url.format(pg)
            self.get_html(url)
            time.sleep(random.uniform(1, 2))


if __name__ == '__main__':
    spider = LianjiaSpider()
    spider.run()
