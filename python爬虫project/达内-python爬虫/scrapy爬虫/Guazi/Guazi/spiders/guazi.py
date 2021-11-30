import scrapy
from ..items import GuaziItem


class GuaziSpider(scrapy.Spider):
    name = 'guazi'
    allowed_domains = ['www.guazi.com']

    # start_urls = ['https://www.guazi.com/beijing/buy/o1/#bread']
    # 去掉start_urls
    # 重写start_requersts()方法
    def start_requests(self):
        for i in range(1, 8):
            url = 'https://www.guazi.com/beijing/buy/o{}/#bread'.format(i)
            # 交给调度器入队列，并制定解析函数
            yield scrapy.Request(url=url, callback=self.detail_page)

    def detail_page(self, response):
        div_list = response.xpath('//div[@class="carlist-content clearfix]/div')
        for div in div_list:
            # 给items.py中的GuaziItem类做实例化
            item = GuaziItem()
            item["name"] = div.xpath('//*[@id="pageWrapper"]/div[1]/div[3]/div[2]/div[1]/div[1]/h5/text()').get()

            # 把抓取的数据提交给管道文件处理：yield item
            yield item

