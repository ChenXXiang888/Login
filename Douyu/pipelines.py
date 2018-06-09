# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline


class DouyuImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        return [Request(x) for x in item.get(self.images_urls_field, [])]

    def item_completed(self, results, item, info):
        if isinstance(item, dict) or self.images_result_field in item.fields:
            item[self.images_result_field] = [x for ok, x in results if ok]
        return item


class DouyuPipeline(object):
    def process_item(self, item, spider):
        return item
