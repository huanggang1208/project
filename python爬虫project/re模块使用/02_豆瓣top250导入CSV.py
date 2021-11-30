# 1.拿到页面源代码
# 2.通过re提取有效信息
import re
import requests
import csv

# 获得网页源代码
start = input("输入页码（页码*25）：")
url = "https://movie.douban.com/top250?start={}&filter=".format(start)
header = {"user-agent": "Mozilla/5.0"}
resp = requests.get(url, headers=header)
page_content = resp.text

# 解析数据
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>'
                 r'.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span '
                 r'class="rating_num" property="v:average">(?P<score>.*?)</span>'
                 r'.*? <span>(?P<pingfenrenshu>.*?)</span>.*?</div>', re.S)
result = obj.finditer(page_content)
f = open("top250.csv", "w", encoding="utf-8")
csvwriter = csv.writer(f)
for i in result:
    # print(i.group("name"))
    # print(i.group("year").strip())
    # print(i.group("score"))
    # print(i.group("pingfenrenshu"))
    dic = i.groupdict()
    dic['year'] = dic['year'].strip()
    csvwriter.writerow(dic.values())

f.close()
resp.close()
print("victory!")
