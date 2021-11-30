# 1.拿到页面源代码
# 2.通过re提取有效信息
import re
import requests

# 获得网页源代码
start = input("输入页码（页码*25）：")
url = "https://movie.douban.com/top250?start={}&filter=".format(start)
header = {"user-agent": "Mozilla/5.0"}
resp = requests.get(url, headers=header)
page_content = resp.text
print(page_content)

# 解析数据
obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>'
                 r'.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span '
                 r'class="rating_num" property="v:average">(?P<score>.*?)</span>'
                 r'.*? <span>(?P<pingfenrenshu>.*?)</span>.*?</div>', re.S)
result = obj.finditer(page_content)
for i in result:
    print(i.group("name"))
    print(i.group("year").strip())
    print(i.group("score"))
    print(i.group("pingfenrenshu"))
resp.close()
print("victory!")
