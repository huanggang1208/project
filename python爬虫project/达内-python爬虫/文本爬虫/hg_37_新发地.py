# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_37_新发地.py
import random

from fake_useragent import UserAgent
import requests
import pymongo
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

# driver = webdriver.Firefox()
# driver.get(url='https://www.douban.com/')
# driver.find_element(By.XPATH, '//*[@id="anony-nav"]/div[3]/form/span[1]/input').send_keys("哈哈哈组")
# time.sleep(2)
# driver.find_element(By.XPATH, '//*[@id="anony-nav"]/div[3]/form/span[2]/input').click()
# time.sleep(2)

# driver.get(url='https://www.xuexi.cn/')
# driver.find_element_by_link_text("用户登录").click()
# time.sleep(5)
# driver.get(url="http://www.xinfadi.com.cn/index.html")
# pages = driver.find_elements(By.XPATH, '//div[@class="tbl-body"]//tr')
# time.sleep(15)
# for page in pages:
#     print(page.text)
#     print("*"*50)

url = "http://www.xinfadi.com.cn/getPriceData.html"
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
    "Connection": "keep-alive",
    "Content-Length": "82",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Host": "www.xinfadi.com.cn",
    "Origin": "http://www.xinfadi.com.cn",
    "Referer": "http://www.xinfadi.com.cn/priceDetail.html",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
                  " Chrome/96.0.4664.45 Safari/537.36",
    "X-Requested-With": "XMLHttpRequest",

}
data = {'limit': 20}
conn = pymongo.MongoClient('localhost', 27017)
db = conn['my_db']
myset = db['xinfadi']
start_time = time.time()
i = 0
for pn in range(1, 100):
    time.sleep(random.uniform(0, 2))
    data['current'] = pn
    html = requests.post(url=url, headers=headers, data=data).json()
    prod_list = []
    for li in html["list"]:
        item = {}
        item["菜名"] = li["prodName"]
        item["type"] = li["prodCat"]
        i += 1
        print(item)
        prod_list.append(item)
        print("*" * 100)
    myset.insert_many(prod_list)
end_time = time.time()
print("爬取%d个" % i)
print(end_time-start_time)
