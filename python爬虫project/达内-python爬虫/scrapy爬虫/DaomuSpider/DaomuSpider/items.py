# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DaomuspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 最终需求数据
    parent_title = scrapy.Field()
    son_title = scrapy.Field()
    novel_content = scrapy.Field()


class DaomuItem:
    pass