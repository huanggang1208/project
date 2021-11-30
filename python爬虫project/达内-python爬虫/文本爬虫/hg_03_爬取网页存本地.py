# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_03_爬取网页存本地.py
# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_02_parse使用.py
from urllib import parse
from urllib import request

wd = input("请输入要查询的名字：")
# URL编码--parse
params = parse.urlencode({"wd": "{}".format(wd)})
# 定义常用变量
url = "http://www.baidu.com/s?" + params
# url = "http://www.baidu.com/s? %s" % params
# url = "http://www.baidu.com/s?{}".format(params)
headers = {"user-agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, "
                         "like Gecko) Version/5.1 Safari/534.50"}
# 2包装请求
req = request.Request(url=url, headers=headers)
# 3发送请求
res = request.urlopen(req)
# 4获取响应内容
html = res.read().decode()
print(html)

# 保存html
document = wd + ".html"
with open("E:/pycharm/project/文档TXT/{}".format(document), "w", encoding="utf-8") as f:
    f.write(html)
