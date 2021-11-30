# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_01_图片爬虫1.py
import os.path
import requests

url = "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fup.enterdesk.com%2Fedpic_source%2F53%2F0a%2Fda" \
      "%2F530adad966630fce548cd408237ff200.jpg&refer=http%3A%2F%2Fup.enterdesk.com&app=2002&size=f9999," \
      "10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1639569280&t=e127d1db91d8119e8d9ce9dfdd5201c2 "
headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"}

# 1.content属性：获取bytes数据类型
html = requests.get(url=url, headers=headers).content

# 2.确定图片保存路径
directory = "./images/"
if not os.path.exists(directory):
    os.makedirs(directory)

# 3.保存到本地
filename = directory + url[-10:] + ".jpg"
with open(filename, "wb") as f:
    f.write(html)
