# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Product(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    images = scrapy.Field()
    price = scrapy.Field()
    description = scrapy.Field()

