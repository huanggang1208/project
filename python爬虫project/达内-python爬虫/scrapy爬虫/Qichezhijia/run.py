# -*- coding = utf8 -*-
# @Author:hggg
# @File:run.py
from scrapy import cmdline

# cmdline.execute('scrapy crawl qichezhijia'.split())
# 直接存入csv，其他管道文件也会执行
cmdline.execute('scrapy crawl qichezhijia -o qichezhijia.csv'.split())

