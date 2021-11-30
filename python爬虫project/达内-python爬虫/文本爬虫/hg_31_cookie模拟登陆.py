# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_31_cookie模拟登陆.py
"""
cookie模拟登陆的方式：利用requests模块的session对象,来实现客户端和服务端的会话保持
原理：实例化session对象：s = requests.session()
    session对象发送get或者post请求
    resp = s.get(url=url, headers=headers)
    resp = s.post(url=url, data=data, headers=headers)

    !!!！1.要知道是哪个服务器返回验证请求，在抓包的时候要输入错误的密码
        2.模拟浏览器利用session对象发送请求验证登录
        3.登录成功，开始抓取需要登录的页面
"""

import requests

s = requests.session()


def login():
    post_url = "https://accounts.douban.com/j/mobile/login/basic"
    get_url = "https://www.douban.com/people/209042263/"
    # 这个cookie要登录成功的cookie
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                             "(KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
        "Cookie": 'douban-fav-remind=1; __gads=ID=3d542780802e38f5-225582d882c400dc:T=1604215881:RT=1604215881:S'
                  '=ALNI_Mb_5JdjCjL5i-IIMIo4QRmm2rp7EA; ll="108288"; bid=NVMM84_OZN4; viewed="35292992"; '
                  'gr_user_id=94d2b785-575b-4ebe-9b3a-9a5f7b9b35ee; push_noty_num=0; push_doumail_num=0; '
                  '_pk_ref.100001.8cb4=%5B%22%22%2C%22%22%2C1637653475%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl'
                  '%3DBGtmdmEEJg3lzoEFq7HB3WQqPwSa9BOyojDSzZo8vVJmnrt5gxgJLCkEl-R1UjKP%26wd%3D%26eqid'
                  '%3Dea0a3d1c000077a600000003619c9bde%22%5D; _pk_ses.100001.8cb4=*; '
                  '__utma=30149280.1279800892.1556521961.1637542896.1637653475.19; __utmc=30149280; '
                  '__utmz=30149280.1637653475.19.7.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; '
                  '__utmv=30149280.20904; ap_v=0,6.0; dbcl2="209042263:twBpXsHHzqQ"; ck=gIpQ; __utmt=1; '
                  '__utmb=30149280.19.10.1637653475; '
                  '_pk_id.100001.8cb4=c8785d5e32e98e31.1542175282.7.1637655469.1636596666. '
    }
    form_data = {
        "ck": "",
        "remember": "true",
        "name": "17585119404",
        "password": "hxg941208#",
        "ticket": "t035uRXdWdQrqodfoDBauJ_FykXcpnUthCSjhDq2SSHkJWt52cWFIAJud7d"
                  "foW_YutdotIWrC0qnzp1ntrHQyWYCrgTtlvpaRRsPyMybJidP4akJhGBPI0"
                  "0T2UuFRrjvnFnOfNwkAgWlL0-lgoHxX_YJipTlGt0H5AHVBvVuXe-8-Y*",
        "randstr": "@RLM",
        "tc_app_id": "2044348370",
    }
    # 先登录
    html = s.post(url=post_url, headers=headers, data=form_data).text
    print(html)

    # 抓取页面
    html = s.get(url=get_url, headers=headers).text
    print(html)


login()

