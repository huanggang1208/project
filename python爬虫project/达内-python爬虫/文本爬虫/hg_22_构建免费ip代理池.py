# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_22_构建免费ip代理池.py
import requests
from lxml import etree



class ProxyPool:
    def __init__(self):
        self.url = "http://www.66ip.cn/{}.html"
        self.test_url = "http://baidu.com/"
        self.headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"}

    def get_proxy_pool(self, url):
        html = requests.get(url=url, headers=self.headers).text
        p = etree.HTML(html)
        # 基准xpath
        tr_list = p.xpath('//div[@id="main"]//tr')
        for tr in tr_list[1:]:
            ip = tr.xpath('./td[1]/text()')[0].strip()
            port = tr.xpath('./td[2]/text()')[0].strip()
            # 测试代理ip是否可用
            self.test_proxy(ip, port)

    def test_proxy(self, ip, port):
        """测试一个ip是否可用"""
        proxys = {
            'http': 'http:{}:{}'.format(ip, port),
            'https': 'https:{}:{}'.format(ip, port)
        }
        try:
            res = requests.get(url=self.test_url, proxies=proxys, headers=self.headers, timeout=2)
            if res.status_code == 200:
                print(ip, port, "\033[31m可用\033[0m")
                # 保存ip
                with open("proxy.txt", "a") as f:
                    f.write(ip + ":" + port + "\n")
        except Exception as e:
            print(ip, port, "不可用")

    def run(self):
        for i in range(1, 101):
            url = self.url.format(i)
            self.get_proxy_pool(url=url)


if __name__ == '__main__':
    spider = ProxyPool()
    spider.run()
