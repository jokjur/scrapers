import scrapy
from ..items import AutopliusSpiderItem

class TestSpider(scrapy.Spider):
    name = "autoplius"
    pages_to_scrape = 5

    start_urls = [
        "https://en.autoplius.lt/ads/used-cars?make_id=99"
    ]

    def parse(self, response):
        urls = response.css('div.auto-lists a::attr(href)').getall()

        for url in urls:
            yield scrapy.Request(url, callback=self.parse_car)

        next_page = response.css('.paging .next').attrib['href']

        if (next_page is not None) and self.pages_to_scrape > 1:
            self.pages_to_scrape -= 1
            yield response.follow(next_page, callback=self.parse)

    def parse_car(self, response):
        items = AutopliusSpiderItem()
        features = {}

        for selector in response.css('div.feature-row'):
            temp = []

            for feature in selector.css('span.feature-item::text').getall():
                temp.append(feature.strip())

            features[selector.css('div.feature-label::text').get().strip()] = temp

        items['Make'] = response.css('script::text').re_first(r'\bvar\s+makeName\s=\s"(.*)".')
        items['Model'] = response.css('script::text').re_first(r'\bvar\s+modelName\s=\s"(.*)".')
        items['Price'] = response.css('div.price::text').get().strip().replace(' ', '')
        items['Mileage'] = ''.join(response.xpath('//div[contains(@class, "parameter-label") and contains(.,  "Mileage")]/..').css('div.parameter-value::text').re(r'[0-9]+'))
        items['Equipment'] = features

        yield items
        