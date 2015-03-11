# -*- coding: utf-8 -*-

import scrapy

from scrapy.selector import Selector
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

from DoubanSpider.items import MovieItem

class MovieSpider(CrawlSpider):
    name = 'movie'
    allowed_domains = ['movie.douban.com']
    start_urls = ['http://movie.douban.com/tag/']

    rules = (
        Rule(LinkExtractor(allow=r'tag'), callback='parse_tag', follow=True),
        Rule(LinkExtractor(allow=r'subject\/\d+\/$'), callback='parse_subject', follow=True),
    )

    def parse_tag(self, response):
        #print response.url
        return

    def parse_subject(self, response):
        #print response.url
        m = MovieItem()
        m['douban'] = response.url
        s = Selector(response).xpath('/html/body/div[@id="wrapper"]/div[@id="content"]')
        m['name'] = s.xpath('./h1/span[1]/text()').extract()
        s = Selector(response).xpath('//div[@id="info"]')
        m['director'] = s.xpath('./span[1]/span[2]/a/text()').extract()
        m['actors'] = s.xpath('./span[@class="actor"]/span[2]//a/text()').extract()
        m['genre'] = s.xpath('./span[@property="v:genre"]/text()').extract()
        m['release_date'] = s.xpath('./span[@property="v:initialReleaseDate"]/text()').extract()
        m['runtime'] = s.xpath('./span[@property="v:runtime"]/text()').extract()
        s = Selector(response).xpath('//div[@id="interest_sectl"]')
        m['score'] = s.xpath('//strong[@property="v:average"]/text()').extract()
        m['num_votes'] = s.xpath('//span[@property="v:votes"]/text()').extract()
        yield m
