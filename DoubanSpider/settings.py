# -*- coding: utf-8 -*-

# Scrapy settings for DoubanSpider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'DoubanSpider'

SPIDER_MODULES = ['DoubanSpider.spiders']
NEWSPIDER_MODULE = 'DoubanSpider.spiders'

DOWNLOADER_MIDDLEWARES = {
    'DoubanSpider.middlewares.RandomUserAgentMiddleware': 400,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
}

DOWNLOAD_DELAY = 1
COOKIES_ENABLED = False
