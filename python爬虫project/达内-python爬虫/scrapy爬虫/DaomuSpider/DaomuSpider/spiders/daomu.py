import scrapy
from ..items import DaomuspiderItem
import os


class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['daomubiji.com']
    start_urls = ['http://www.daomubiji.com/']

    def parse(self, response):
        # 提取一级页面：大标题、大链接
        a_list = response.xpath('//li[contains(@id, "menu-item-2")]/a')
        for a in a_list:
            item = DaomuspiderItem()
            item["parent_title"] = a.xpath('./text()').get().replace('：', '_')
            parent_href = a.xpath('./@href').get()
            print("大标题" + item["parent_title"])
            print("大链接" + parent_href)
            # 创建对应的结构目录
            # os.mkdir('./novel/盗墓笔记1_七星鲁王')
            directory = './novel/{}'.format(item["parent_title"])
            if not os.path.exists(directory):
                os.mkdir(directory)

            # 将小链接继续交个调度器入队列
            yield scrapy.Request(url=parent_href, meta={'item': item}, callback=self.parse_second_page)

    def parse_second_page(self, response):
        # 提取小标题、小链接
        meta1 = response.meta["item"]
        a_list = response.xpath('//div[@class="excerpts-wrapper"]/div[1]/article/a')
        for a in a_list:
            # 创建新的item对象，避免给对象赋值是被覆盖
            item = DaomuspiderItem()
            item["son_title"] = a.xpath('./text()').get()
            item["parent_title"] = meta1["parent_title"]
            son_href = a.xpath('./@href').get()
            # print(son_href)

            # 将son_href交给调度器
            yield scrapy.Request(url=son_href, meta={'item': item}, callback=self.parse_third_page)

    def parse_third_page(self, response):
        """提小说"""
        item = response.meta["item"]
        # extract()是序列化提取所有、get()是序列化提取第一个
        p_list = response.xpath('//article/p/text()').extract()
        item["novel_content"] = '\n'.join(p_list)
        # 小说抓取完成，交给管道文件
        yield item




