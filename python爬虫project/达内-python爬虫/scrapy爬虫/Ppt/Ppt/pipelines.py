# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline
import scrapy
import os


class PptPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        """将文件下载链接交给调度器入队列"""
        yield scrapy.Request(url=item['ppt_download_url'], meta={'item': item})

    def file_path(self, request, response=None, info=None, *, item=None):
        """重写文件名和保存路径"""
        item = response.meta["item"]
        filename = '{}/{}{}'.format(
            item['class_name'],
            item['ppt_name'],
            # os.path.splitext(item['ppt_download_url'])[1]取文件后缀名称
            os.path.splitext(item['ppt_download_url'])[1]
        )

        return filename






