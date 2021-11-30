# -*- coding = utf8 -*-
# @Author:hggg
# @File:hg_30_线程池腾讯招聘.py
import requests
from fake_useragent import UserAgent
import time
from concurrent.futures import ThreadPoolExecutor

class Tencent:
    def __init__(self):

        self.i = 0
        self.url1 = "https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1637579279985&countryId" \
                    "=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword={}&pageIndex={" \
                    "}&pageSize=10&language=zh-cn&area=cn "
        self.url2 = "https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1637579364282&postId={" \
                    "}&language=zh-cn "
        self.headers = {"user-agent": UserAgent().random}

    def parse_one(self, keyword, page):
        html1 = requests.get(url=self.url1.format(keyword, page), headers=self.headers).json()
        for one_job in html1["Data"]["Posts"]:
            post_id = one_job["PostId"]
            # 拼接二级url
            job_url = self.url2.format(post_id)
            html2 = requests.get(url=job_url, headers=self.headers).json()
            item = {}
            item["name"] = html2["Data"]["RecruitPostName"]
            item["place"] = html2["Data"]["LocationName"]
            item["type"] = html2["Data"]["CategoryName"]
            item["require"] = html2["Data"]["Requirement"]
            item["time"] = html2["Data"]["LastUpdateTime"]
            print(item)
            self.i += 1

    def main(self):
        keyword = input("需要抓什么职位：")
        start_time = time.time()
        url = "https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1637579279985&countryId" \
              "=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword={}&pageIndex={" \
              "}&pageSize=10&language=zh-cn&area=cn "
        url = url.format(keyword, 1)
        headers = {"user-agent": UserAgent().random}
        html = requests.get(url=url, headers=headers).json()
        count = html["Data"]["Count"]
        total = count // 10 if count % 10 == 0 else count // 10 + 1
        pool = ThreadPoolExecutor(max_workers=15)
        for page in range(1, total + 1):
            pool.submit(self.parse_one(keyword=keyword, page=page))
        pool.shutdown()
        end_time = time.time()
        print("抓取%d条职位信息" % self.i)
        print("计时%.2f" % (end_time - start_time))



if __name__ == '__main__':
    spider = Tencent()
    spider.main()



