# -*- coding: utf-8 -*-
import json

import scrapy

from Douyu.items import DouyuItem


class DouyuSpider(scrapy.Spider):
    name = "douyu"
    allowed_domains = ["douyucdn.cn"]
    global base_url
    base_url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=100&offset="
    offset = 0
    start_urls = [base_url + str(offset)]

    def parse(self, response):
        """获取想要的字段"""
        data_list = json.loads(response.body)["data"]
        if not data_list:
            return
        for data in data_list:
            item = DouyuItem()
            item["room_link"] = "http://www.douyu.com/" + data["room_id"]
            item["image_link"] = data["vertical_src"]
            item["nick_name"] = data["nickname"]
            item["anchor_city"] = data["anchor_city"]
            yield item
        # 获取url 构建请求函数交给调度器
        self.offset += 100
        yield scrapy.Request(base_url + str(self.offset), callback=self.parse)
