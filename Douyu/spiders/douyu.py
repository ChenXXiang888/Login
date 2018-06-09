# -*- coding: utf-8 -*-
import scrapy


class DouyuSpider(scrapy.Spider):
    name = "douyu"
    allowed_domains = ["douyucdn.cn"]
    start_urls = (
        'http://www.douyucdn.cn/',
    )

    def parse(self, response):
        pass
