# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_35_selenium操作鼠标.py
"""
selenium操作鼠标：
打开浏览器，输入百度url，鼠标移动到右上角-设置-点击高级搜索
"""
# 导入鼠标类
import time

from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By

# 打开浏览器输入url
driver = webdriver.Firefox()
driver.get(url='http://baidu.com/')
# 移动到设置节点
set_node = driver.find_element(By.XPATH, '//*[@id="s-usersetting-top"]')
ActionChains(driver).move_to_element(to_element=set_node).perform()

# 找到高级搜索并点击
driver.find_element(By.LINK_TEXT, '高级搜索').click()
time.sleep(8)
driver.quit()
