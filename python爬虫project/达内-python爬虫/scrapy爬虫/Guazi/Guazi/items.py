# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GuaziItem(scrapy.Item):
    # define the fields for your item here like:
    # 需要汽车的名称、价格、链接
    # name = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    link = scrapy.Field()


"""相当于定义了一个字典，但是只给了key，没有给value"""
