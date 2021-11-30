# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_33_selenium爬猫眼100.py
"""
使用selenium抓取猫眼100
"""
from selenium import webdriver
from selenium.webdriver.common.by import By


"""# 实现无界面化操作
options = webdriver.FirefoxOptions()
# 添加无界面功能
options.add_argument('--headless')

driver = webdriver.Firefox(options=options)"""
driver = webdriver.Firefox()
driver.get(url='https://www.maoyan.com/board/4')


def get_one_url():
    # 基准xpath：匹配每个电影信息的dd节点对象列表
    dd_list = driver.find_elements(By.XPATH, '//*[@id="app"]/div/div/div[1]/dl/dd')
    for dd in dd_list:
        # text属性是获取当前dd节点以及他的子节点和后代节点的文本内容
        one_film_info_list = dd.text.split('\n')
        item = {}
        item["排名"] = one_film_info_list[0].strip()
        item["电影名字"] = one_film_info_list[1].strip()
        item["主演"] = one_film_info_list[2].strip()
        item["上映时间"] = one_film_info_list[3].strip()
        item["评分"] = one_film_info_list[4].strip()
        print(item)
        print('*' * 50)


while True:
    get_one_url()
    try:
        # selenium找节点，如果没有找到就会抛出异常
        driver.find_element(By.LINK_TEXT, '下一页').click()
    except Exception as e:
        driver.quit()
        break


