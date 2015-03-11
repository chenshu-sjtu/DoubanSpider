# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MovieItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    director = scrapy.Field()
    actors = scrapy.Field()
    genre = scrapy.Field()
    release_date = scrapy.Field()
    runtime = scrapy.Field()
    score = scrapy.Field()
    num_votes = scrapy.Field()
    douban = scrapy.Field()
