# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from scraper.items import ExcelItem


class PermitSpider(scrapy.Spider):
    name = 'permits'
    start_urls = ['https://www.denvergov.org/content/denvergov/en/denver-development-services/help-me-find-/building-permits.html']  # NOQA

    def parse(self, response):
        loader = ItemLoader(item=ExcelItem(), response=response)
        base_url = 'https://www.denvergov.org'
        xls_files = response.css('li a[href$=".xls"]::attr(href)').getall()

        for link in xls_files:
            absolute_link = base_url + link
            double_link = 'https://www.denvergov.orghttps://www.denvergov.org'

            if double_link in absolute_link:
                absolute_link = absolute_link[25:]

            loader.add_value('file_urls', absolute_link)
            yield loader.load_item()
