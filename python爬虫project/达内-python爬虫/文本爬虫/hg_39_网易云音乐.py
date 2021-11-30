# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_39_网易云音乐.py
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
import pymongo

# 存入mongodb
conn = pymongo.MongoClient("localhost", 27017)
db = conn["my_db"]
myset = db["网易"]

# 设置成无界面
options = webdriver.FirefoxOptions()
options.add_argument("--headless")
driver = webdriver.Firefox(options=options)
start = time.time()
driver.get(url='https://music.163.com/')
driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div/ul/li[2]/a/em').click()

# 切换到子页面，找frame节点
time.sleep(3)
frame_node = driver.find_element(By.XPATH, '//*[@id="g_iframe"]')
driver.switch_to.frame(frame_node)
# 第二种方式：driver.switch_to.frame("contenFrame")

# 查找需求
tr_list = driver.find_elements(By.XPATH, '//table/tbody/tr')
dic_list = []
for tr in tr_list:
    item = {}
    item["rank"] = tr.find_element(By.XPATH, './/span[@class="num"]').text.strip()
    # get_attribute:获取某个节点的属性值
    item["song"] = tr.find_element(By.XPATH, './/span[@class="txt"]/a/b').get_attribute("title").strip().replace("\xa0", " ")
    item["singer"] = tr.find_element(By.XPATH, './/div[@class="text"]/span').get_attribute("title").strip()
    print(item)
    dic_list.append(item)
myset.insert_many(dic_list)

end = time.time()
print(end-start)
driver.quit()


