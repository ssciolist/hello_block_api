# -*- coding: utf-8 -*-
import scrapy


class ExcelItem(scrapy.Item):
    file_urls = scrapy.Field()
    file_name = scrapy.Field()
    files = scrapy.Field()
