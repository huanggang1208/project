# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_36_selenium爬民政部.py
import csv
import time
import pymongo
from selenium.webdriver.common.by import By
from selenium import webdriver


class SpiderMzb:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url='http://www.mca.gov.cn/article/sj/xzqh/1980/')
        self.headers = ["城市", "邮编"]
        self.f = open("区域规划.csv", "a", encoding="utf-8", newline="")
        self.writer = csv.DictWriter(self.f, self.headers)
        self.writer.writeheader()

    def parse_html(self):
        # 最新月份的节点
        new_node = self.driver.find_element(By.XPATH,
                                            '//*[@id="list_content"]/div[2]/div/ul/table/tbody/tr[1]/td[2]/a')
        new_node.click()
        # 切换句柄（页面）
        li = self.driver.window_handles
        self.driver.switch_to.window(li[1])
        time.sleep(1)
        self.driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div[2]/div[2]/p[1]/a').click()

        # 提取数据
        tr_list = self.driver.find_elements(By.XPATH, '//table//tr')
        item = {}
        for tr in tr_list[3:-4]:
            try:
                item["邮编"] = tr.text.split()[0].strip()
                item["城市"] = tr.text.split()[1].strip()
                self.writer.writerow(item)
                print(item)

            except Exception as e:
                print(e)
                pass
            continue

    def run(self):
        self.parse_html()
        self.f.close()


if __name__ == '__main__':
    spider = SpiderMzb()
    spider.run()




