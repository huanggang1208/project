import requests
import re
import csv


url = "https://music.douban.com/top250"
header = {"user-agent": "Mozilla/5.0"}
kw = {
        'start': '25'
    }
resp = requests.get(url, headers=header, data=kw)
text = resp.text

re_obj = re.compile(r' <a class="nbg".*?alt="(?P<singer>.*?) - (?P<song>.*?)" style="width'
                 r': 80px; max-height: 120px;" />.*? </span></div>', re.S)
result = re_obj.finditer(text)

# 创建一个CSV文件
f = open("豆瓣音乐top250.csv", "w", encoding="utf-8", newline="")
# 基于文件对象写入数据
writer = csv.writer(f)
# 穿件文件表头
writer.writerow(['singer', 'song'])
for i in result:
    dic = i.groupdict()
    writer.writerow(dic.values())

f.close()
resp.close()


