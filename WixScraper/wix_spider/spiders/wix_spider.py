import scrapy
import os
import shutil
from ..items import WixSpiderItem

def delete_previous():
    if 'text.json' in os.listdir('.'):
        os.remove('./text.json')

    if 'images' in os.listdir('.'):
        shutil.rmtree('./images')

class WixSpider(scrapy.Spider):
    name = 'wix'

    delete_previous()

    start_urls = ["https://mekass.wixsite.com/website"]

    def parse(self, response):
        item = WixSpiderItem()

        text = response.xpath('//body//*[not(self::style or  self::script)]/text()').getall()
        images = response.css('img::attr(src)').extract()

        item['text'] = [i.strip() for i in text if i.strip() != "" ]
        item["image_urls"] = [img.split('/v1')[0] for img in images]
        
        yield item

