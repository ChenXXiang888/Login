# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import os
import scrapy
from scrapy.pipelines.images import ImagesPipeline

from Douyu.settings import IMAGES_STORE


class DouyuImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # return [Request(x) for x in item.get(self.images_urls_field, [])]
        yield scrapy.Request(item["image_link"])

    def item_completed(self, results, item, info):
        # if isinstance(item, dict) or self.images_result_field in item.fields:
        #     item[self.images_result_field] = [x for ok, x in results if ok]
        """
        [(True, {'url': 'https://rpic.douyucdn.cn/live-cover/appCovers/2018/05/29/3735665_20180529193655_big.jpg',
        'path': 'full/7aaa3d4be1e9835206e18c8cc86e4968b4b812bd.jpg',
        'checksum': '2e4659cfcce6b0e1518895225d2f5577'})]
        """
        # 原始图片保存路径
        source_path = IMAGES_STORE + [x['path'] for ok, x in results if ok][0]
        # 现在新的图片保存路径
        item['image_path'] = IMAGES_STORE + item["nick_name"] + ".jpg"
        try:
            os.rename(source_path, item['image_path'])
        except Exception as e:
            print (e)
            logging.error('Image %s rename failed' % source_path)
        return item
