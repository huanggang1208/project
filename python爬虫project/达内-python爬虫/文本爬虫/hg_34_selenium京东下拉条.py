# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_34_selenium京东下拉条.py
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pymongo


class JdSpider:
    def __init__(self):
        # 设置无界面
        self.options = webdriver.FirefoxOptions()
        self.options.add_argument("--headless")
        self.driver = webdriver.Firefox(options=self.options)
        # 有界面
        # self.driver = webdriver.Firefox()
        self.driver.get(url="https://www.jd.com/")
        # 点击搜索框，点击
        self.driver.find_element(By.XPATH, '//*[@id="key"]').send_keys("爬虫书")
        self.driver.find_element(By.XPATH, '//*[@id="search"]/div/div[2]/button').click()
        # 给页面停留加载时间
        time.sleep(1)
        # 创建MongoDB变量
        self.conn = pymongo.MongoClient('localhost', 27017)
        self.db = self.conn['jddb']
        self.myset = self.db['jdset']

    def parse_html(self):
        # 提取具体数据
        # 先把滚动条拉到最下,等到所有数据加载完成在进行数据提取
        self.driver.execute_script(
            'window.scrollTo(0,document.body.scrollHeight)'
        )
        time.sleep(3)
        # 提取具体数据
        li_list = self.driver.find_elements(By.XPATH, '//*[@id="J_goodsList"]/ul/li')
        try:
            item = {}
            for li in li_list:
                item["价格"] = li.find_element(By.XPATH, './/div[@class="p-price"]/strong').text.strip()
                item["名字"] = li.find_element(By.XPATH, './/div[@class="p-name"]/a/em').text.strip()
                print(item)
                self.myset.insert_one(item)
                print("*"*50)
        except Exception as e:
            print(e)

    def run(self):
        while True:
            self.parse_html()
            # 没有找到节点内容为"pn-next disabled"的说明不是最后一页就需要点击下一页开始抓取
            if self.driver.page_source.find("pn-next disabled") == -1:
                self.driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[2]/div[1]/div/div[3]/div/span[1]/a[9]').click()
                time.sleep(2)
            else:
                time.sleep(2)
                self.driver.quit()
                break


if __name__ == '__main__':
    spider = JdSpider()
    spider.run()