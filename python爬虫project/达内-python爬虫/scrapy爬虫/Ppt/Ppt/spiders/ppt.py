import scrapy
from ..items import PptItem


class PptSpider(scrapy.Spider):
    name = 'ppt'
    allowed_domains = ['www.1ppt.com']
    start_urls = ['http://www.1ppt.com/xiazai/']

    def parse(self, response):
        print(response.text)
        """一级页面爬取函数：29个分类和链接"""
        li_list = response.xpath('//div[@class="col_nav clearfix"]/ul/li')
        print(li_list)
        for li in li_list[1:]:
            item = PptItem()
            item["class_name"] = li.xpath('./a/text()').get()
            class_href = 'http://www.1ppt.com' + li.xpath('./a/@href').get()

            # 交给调度器入队列
            yield scrapy.Request(url=class_href, meta={'meta1': item}, callback=self.parse_second_page)

    def parse_second_page(self, response):
        """二节页面解析函数：20个ppt名称和链接"""
        meta1 = response.meta['meta1']
        # 提取
        li_list = response.xpath('//ul[@class="tplist"]/li')
        for li in li_list:
            item = PptItem()
            item["ppt_name"] = li.xpath('./h2/a/text()').get()
            item["class_name"] = meta1["class_name"]
            ppt_info_list = 'http://www.1ppt.com' + li.xpath('./h2/a/@href').get()

            # 交给调度器入队列
            yield scrapy.Request(url=ppt_info_list, meta={'meta2': item}, callback=self.parse_third_page)

    def parse_third_page(self, response):
        """解析三级页面：进入下载页的链接"""
        meta2 = response.meta['meta2']
        enter_download_page = 'http://www.1ppt.com' + response.xpath('//ul[@class="downurllist"]/li/a/@href').get()

        # 交给调度器入队列
        yield scrapy.Request(url=enter_download_page, meta={'item': meta2}, callback=self.parse_forth_page)

    def parse_forth_page(self, response):
        """四级页面，获取下载链接"""
        item = response.meta['item']
        item['ppt_download_url'] = response.xpath('//ul[@class="downloadlist"]/li[1]/a/@href').get()

        # 一个完整的链接提取完成
        yield item




