# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_32_selenium.py
from selenium import webdriver
from selenium.webdriver.common.by import By

# 实例化一个浏览器驱动器并打开百度网址
driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")

# 通过xpath路径找到搜索框，发送关键字，点击百度一下按钮
driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys('赵丽颖')
driver.find_element(By.XPATH, '//*[@id="su"]').click()

# 1 获取屏幕截图
driver.save_screenshot("baidu.png")
# 2 浏览器窗口最大化
driver.maximize_window()
# 3 .quit():关闭浏览器
driver.quit()
# 4 .page_source:HTML结构源码
html = driver.page_source
# 5 .find():在HTML结构源码中查找每个字符串是否存在，查找失败返回-1
#           经常用来判断是否是最后一页
driver.page_source.find("huanggang")
