# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_38_selenium模拟登陆QQ.py
import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()
driver.get(url='https://mail.qq.com/')
"""
第一种方法:找到第一级页面的frame节点，然后切换到这个节点开始下一步操作

frame_node = driver.find_element(By.XPATH, '//*[@id="login_frame"]')
driver.switch_to.frame(frame_node)
"""

# 第二种方法：如果在第一级页面的frame节点中有id、name属性，可以直接操作切换
driver.switch_to.frame('login_frame')
driver.find_element(By.XPATH, '//*[@id="u"]').send_keys('1196361777@qq.com')
driver.find_element(By.ID, 'p').send_keys('huang19941208@')
time.sleep(0.7)
driver.find_element(By.XPATH, '//*[@id="login_button"]').click()

