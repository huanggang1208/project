# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_01_httpbin.py

# """使用Request包装网址"""
# from urllib import request
# # 1定义常用变量
# url = "http://httpbin.org/get"
# headers = {"user-agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, "
#                          "like Gecko) Version/5.1 Safari/534.50"}
# # 2包装请求
# req = request.Request(url=url, headers=headers)
# # 3发送请求
# res = request.urlopen(req)
# # 4获取响应内容
# html = res.read().decode()
# print(html)
import requests
import json

url = "https://prod.api.xiaomi.cn/community/square?start=2&limit=10"
headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"}
# data = {'Cookie': 'douban-fav-remind=1; __gads=ID=3d542780802e38f5-225582d882c400dc:T=1604215881:RT'
#                                '=1604215881:S=ALNI_Mb_5JdjCjL5i-IIMIo4QRmm2rp7EA; ll="108288"; bid=NVMM84_OZN4; '
#                                '_vwo_uuid_v2=DA4FB0B92BE1BAB34414418E5B5CF9FF1|302202f6bed70244a65b06cd7380ddab; '
#                                'viewed="35292992"; gr_user_id=94d2b785-575b-4ebe-9b3a-9a5f7b9b35ee; '
#                                '__yadk_uid=DZRzoUbQqLqMEnoOZgpIHuYdVMbXKtNl; dbcl2="209042263:GdqZyAUX5xE"; '
#                                'push_noty_num=0; push_doumail_num=0; '
#                                '__utmz=30149280.1637498093.17.6.utmcsr=open.weixin.qq.com|utmccn=('
#                                'referral)|utmcmd=referral|utmcct=/; ck=462L; '
#                                '_pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1637542896%2C%22https%3A%2F%2Fwww.baidu.com'
#                                '%2Fs%3Fie%3DUTF-8%26wd%3D%25E8%25B1%2586%25E7%2593%25A3%22%5D; _pk_ses.100001.4cf6=*; '
#                                '__utma=30149280.1279800892.1556521961.1637498093.1637542896.18; '
#                                '__utmb=30149280.0.10.1637542896; __utmc=30149280; '
#                                '__utma=223695111.1596328959.1556521961.1637498093.1637542896.14; '
#                                '__utmb=223695111.0.10.1637542896; __utmc=223695111; '
#                                '__utmz=223695111.1637542896.14.8.utmcsr=baidu|utmccn=('
#                                'organic)|utmcmd=organic|utmctr=%E8%B1%86%E7%93%A3; '
#                                '_pk_id.100001.4cf6=00b9b32232f9e06c.1556521961.14.1637542901.1637498093.'}

html0 = requests.get(url=url, headers=headers).text
print(html0)
html = json.loads(html0)
print(html)
