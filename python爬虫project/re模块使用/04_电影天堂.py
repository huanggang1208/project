import requests
import re
import csv


url = "https://www.dy2018.com/"
resp = requests.get(url)
resp.encoding = "gbk"

# 定位2021必看热片
obj1 = re.compile(r'2021必看热片.*?<ul>(?P<movie_info>.*?)</ul>', re.S)
obj2 = re.compile(r"<a href='(?P<lianjie>.*?)'", re.S)
obj3 = re.compile(r'◎片　　名　(?P<movie_name>.*?)<br />◎年　　代　(?P<date>.*?)<br />◎产　　地.*?'
                  r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<dress>.*?)">', re.S)
result1 = obj1.finditer(resp.text)
zilianjie_list = []
for i1 in result1:
    movie_info = i1.group("movie_info")
    result2 = obj2.finditer(movie_info)
    # 提取子页面的内容
    for i2 in result2:
        lianjie = i2.group("lianjie")
        # 拼接子页面，并除去开头/
        zilianjie = url + lianjie.strip("/")
        zilianjie_list.append(zilianjie)  # 把子链接保存到列表里

# 提取子页面链接,并提取子链接里的内容
for herf in zilianjie_list:
    child_resp = requests.get(herf, verify=False)
    child_resp.encoding = 'gbk'
    url_text = child_resp.text
    result3 = obj3.search(url_text)
    print(result3.group("movie_name"))
    print(result3.group("date"))
    print(result3.group("dress"))


