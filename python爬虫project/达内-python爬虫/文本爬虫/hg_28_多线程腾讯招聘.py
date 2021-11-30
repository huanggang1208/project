# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_28_多线程腾讯招聘.py
import requests
import time
from threading import Thread, Lock
from queue import Queue
from urllib import parse
from fake_useragent import UserAgent


class TencentSpider:
    def __init__(self):
        self.one_url = "https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1637579279985&countryId" \
                       "=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword={}&pageIndex={" \
                       "}&pageSize=10&language=zh-cn&area=cn "
        self.two_url = "https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1637579364282&postId={" \
                       "}&language=zh-cn "
        # 两个队列
        self.one_q = Queue()
        self.two_q = Queue()
        # 两把锁
        self.lock1 = Lock()
        self.lock2 = Lock()
        # 计数
        self.num = 0

    def get_html(self, url):
        headers = {"user-agent": UserAgent().random}
        html = requests.get(url=url, headers=headers).json()

        return html

    def url_in(self):
        """一级页面url入队列"""
        keyword = input("请输入职位类别：")
        keyword = parse.quote(keyword)
        # 获取总页数
        total = self.get_total(keyword)
        for page in range(1, total+1):
            url = self.one_url.format(keyword, page)
            self.one_q.put(url)

    def get_total(self, keyword):
        """获取某个类别的总页数"""
        url = self.one_url.format(keyword, 1)
        html = self.get_html(url)
        count = html["Data"]["Count"]
        total = count//10 if count % 10 == 0 else count//10 + 1

        return total

    def parse_one_page(self):
        """解析一级页面：提取postID，拼接二级页面url地址入队列"""
        while True:
            # 加锁
            self.lock1.acquire()
            if not self.one_q.empty():
                one_url = self.one_q.get()
                # 释放锁
                self.lock1.release()
                one_html = self.get_html(url=one_url)
                # one_html一页中有十个postID
                for one_job in one_html["Data"]["Posts"]:
                    post_id = one_job["PostId"]
                    # 拼接二级url
                    job_url = self.two_url.format(post_id)
                    # 入第二个队列
                    self.two_q.put(job_url)
            else:
                self.lock1.release()
                break

    def parse_two_page(self):
        """解析二姐页面：提取具体的职位信息"""
        while True:
            try:
                self.lock2.acquire()
                two_url = self.two_q.get(timeout=1)
                self.lock2.release()
                two_html = self.get_html(two_url)
                item = {}
                item["name"] = two_html["Data"]["RecruitPostName"]
                item["place"] = two_html["Data"]["LocationName"]
                item["type"] = two_html["Data"]["CategoryName"]
                item["require"] = two_html["Data"]["Requirement"]
                item["time"] = two_html["Data"]["LastUpdateTime"]
                print(item)

                self.lock2.acquire()
                self.num += 1
                self.lock2.release()

            except Exception as e:
                self.lock2.release()
                break

    def run(self):
        """程序入口函数"""
        start_time = time.time()
        self.url_in()
        # 创建两个多线程
        t1_list = []
        t2_list = []
        for i in range(5):
            t1 = Thread(target=self.parse_one_page)
            t1_list.append(t1)
            t1.start()

        for i in range(5):
            t2 = Thread(target=self.parse_two_page)
            t2_list.append(t2)
            t2.start()
        for t1 in t1_list:
            t1.join()

        for t2 in t2_list:
            t2.join()

        end_time = time.time()
        print("总数：%d" % self.num)
        print("time:%.2f" % (end_time - start_time))


if __name__ == '__main__':
    spider = TencentSpider()
    spider.run()






