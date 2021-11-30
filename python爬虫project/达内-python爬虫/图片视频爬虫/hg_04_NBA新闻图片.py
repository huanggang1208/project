import requests
from lxml import etree

headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0"}
resq = requests.get(url="https://sports.sohu.com/s/nba?spm=smpc.home.top-nav.8.1637373825701NpCKUKM", headers=headers)
resq.encoding = "utf-8"
html = resq.text
e = etree.HTML(html)
href_list = e.xpath('//li[@class="sports-team-stock"]/ul/li/a/@href')
for href in href_list:
    info_html = requests.get(url=href, headers=headers).text
    p = etree.HTML(info_html)
    image_list = p.xpath('//article[@class="article"]/p[@class="ql-align-center"]/img/@src')
    for image in image_list:
        image_html = requests.get(url=image, headers=headers).content
        filename = "E:/pycharm/project/python爬虫project/达内-python爬虫/图片视频爬虫/images/" + image[-10:]
        with open(filename, "wb") as f:
            f.write(image_html)
