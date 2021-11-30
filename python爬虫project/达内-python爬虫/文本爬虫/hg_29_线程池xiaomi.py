# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_29_线程池xiaomi.py
from queue import Queue
from concurrent.futures import ThreadPoolExecutor
import time
import random
import requests
from fake_useragent import UserAgent


def getting(num):

    url0 = "https://prod.api.xiaomi.cn/community/square?start={}&limit=10"
    headers = {"user-agent": UserAgent().random}
    global i
    i = 0
    for page in range(num):
        base_url = url0.format(page)
        print(base_url)
        html = requests.get(url=base_url, headers=headers).json()
        item = {}
        for record in html["entity"]["records"]:
            item["id"] = record["id"]

            print(item)
            i += 1


def main():
    num = int(input("要抓的页数"))
    pool = ThreadPoolExecutor(max_workers=10)

    pool.submit(getting(num))
    pool.shutdown()


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("抓取%d条信息" % i)
    end_time = time.time()
    print(end_time - start_time)
