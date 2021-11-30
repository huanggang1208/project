import scrapy
from ..items import QichezhijiaItem


class QichezhijiaSpider(scrapy.Spider):
    name = 'qichezhijia'
    allowed_domains = ['www.che168.com']

    def start_requests(self):
        for i in range(1, 2):
            url = 'https://www.che168.com/beijing/a0_0msdgscncgpi1lto{}cspexx0/'.format(i)
            # 交给调度器入队列，并指定解析器
            yield scrapy.Request(url=url, callback=self.detail_page)

    def detail_page(self, response):
        li_list = response.xpath('//div[@class="content fn-clear card-wrap"]//li[@name="lazyloadcpc"]')
        for li in li_list:
            item = QichezhijiaItem()
            item["name"] = li.xpath('.//h4[@class="card-name"]/text()').get()
            item["price"] = li.xpath('.//div[@class="cards-price-box"]//em/text()').get()
            item["link"] = "https://www.che168.com" + li.xpath('./a/@href').get()

            # 把每辆汽车详情页的连接交给调度器入队列
            # meta参数：在不同的解析函数中传递数据
            # 一级页面就直接yield item
            yield scrapy.Request(url=item["link"], meta={'item': item}, callback=self.get_car_info)

    def get_car_info(self, response):
        # meta会随着response一起回来作为response的属性
        item = response.meta['item']
        item["km"] = response.xpath('//ul[@class="brand-unit-item fn-clear"]/li[1]/h4/text()').get()
        item["time"] = response.xpath('//ul[@class="brand-unit-item fn-clear"]/li[2]/h4/text()').get()
        item["typ"] = response.xpath('//ul[@class="brand-unit-item fn-clear"]/li[3]/h4/text()').get()
        item["place"] = response.xpath('//ul[@class="brand-unit-item fn-clear"]/li[4]/h4/text()').get()

        yield item

