# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapingHubItem(scrapy.Item):
    # define the fields
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()
