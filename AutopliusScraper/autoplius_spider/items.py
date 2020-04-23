# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AutopliusSpiderItem(scrapy.Item):
    Make = scrapy.Field()
    Model = scrapy.Field()
    Price = scrapy.Field()
    Mileage = scrapy.Field()
    Equipment = scrapy.Field()
    Url = scrapy.Field()
