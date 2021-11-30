import scrapy


class BaiduSpider(scrapy.Spider):
    # 爬虫名：执行爬虫时使用：scrapy crawl 爬虫名
    name = 'baidu'
    # 允许爬取的域名：scrapy genspider baidu www.baidu.com
    allowed_domains = ['www.baidu.com']
    # 起始的url地址
    start_urls = ['http://www.baidu.com/']

    # 解析提取数据的函数
    def parse(self, response):
        """提取解析数据--百度一下，你就知道"""
        item = {}
        # response.xpath()结果：[<Selector xpath='/html/head/title/text()' data='百度一下，你就知道'>]
        # extract()结果：['百度一下，你就知道']
        # extract_first()结果：'百度一下，你就知道‘，序列化提取第一个
        # get() == extract_first()
        item["title"] = response.xpath('/html/head/title/text()').get()
        print(item)
