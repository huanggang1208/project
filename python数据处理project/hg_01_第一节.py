import random
import time
import os
from typing import Pattern
import requests
from fake_useragent import UserAgent
from lxml import etree
import re

url = 'http://www.daomubiji.com/'
headers = {
    "User-Agent": UserAgent().random
}

html_1 = requests.get(url=url, headers=headers).text
# print(html)
p1 = etree.HTML(html_1)
a_list = p1.xpath(
    '//article[@class="article-content"]')

for a in a_list:
    class_names = a.xpath('.//div[@class="homebook"]/h2/text()')
    hrefs = a.xpath('.//a/@href')
    # print(class_names, '\n', hrefs)
    for href in hrefs:
        html_2 = requests.get(url=href, headers=headers).text
        # print(html_2)
        p2 = etree.HTML(html_2)
        div_list = p2.xpath('//div[@class="excerpts"]/article')

        for div in div_list:
            program_name = div.xpath('./a/text()')
            detail_hrefs = div.xpath('./a/@href')
            # time.sleep(random.uniform(0, 1))
            # print(program_name, detail_hrefs)
            for detail_href in detail_hrefs:
                html_3 = requests.get(url=detail_href, headers=headers).text
                print(html_3)
                regex = '<meta http-equiv .*?<title > (.*?) < /title >'
                pattern = re.compile(regex, re.S)
                header = pattern.findall(html_3)
                print(header)
                # class_name = header[0].split(" ")[0]
                # prangraf_name = header[0].split(" ")[1]
                # txt = header[0].split(" ")[2]

                # directory = './novel/{}/'.format(class_name)
                # if not os.path.exists(directory):
                #     os.mkdir(directory)

                # filename = './novel/{}/{}_{}.txt'.format(
                #     class_name, prangraf_name, txt)
                # p3 = etree.HTML(html_3)
                # detail_novel = p3.xpath(
                #     '//article[@class="article-content"]/p/text()')
                # with open(filename, "w", encoding="utf-8") as f:
                #     f.write(detail_novel)

