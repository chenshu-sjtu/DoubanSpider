============
DoubanSpider
============

This is a Scrapy-based, lightweight web-spider.

It can crawl some interesting materials from douban(豆瓣, http://www.douban.com).

Requirements
============

* Scrapy (`https://github.com/scrapy/scrapy`)

Install
=======

* `git clone git@github.com:chenshu-sjtu/DoubanSpider.git`

Usage Example
=====

* collect all movies
```bash
cd DoubanSpider
scrapy crawl movie -o movies.csv -t csv
```
when it finished (which may take some time), all movie infos will be stored into a .csv file.

How to customize it?
====================

1. Define the structure of items to be scraped in `DoubanSpider/items.py`.
  ```python
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
  ```

2. Define how to crawl these items in `DoubanSpider/spiders/[your-spider-name].py`.
  ```python
  class MovieSpider(CrawlSpider):
    name = ...
    allowed_domains = ...
    start_urls = ...
    rules = (...)
    
    def parse_XXX(...):
      ...
  ```
You can find a more detailed documentation at http://scrapy.org/doc/ 

How to avoid being BANNED?
==========================

douban has some anti-crawler-strategies, so try to be as polite as possible.

1. Do not send requests too frequently.
  ```python
  # DoubanSpider/settings.py
  DOWNLOAD_DELAY = 1.0
  ```
  
2. Turn off the cookies.
  ```python
  # DoubanSpider/settings.py
  COOKIES_ENABLED = False
  ```
  
3. Rotate your USER-AGENTs.
  * in `DoubanSpider/agents.py`, you can find a very long list of available agents.
  * use a different USER-AGENT in http-header when you lunch a new request.

    ```python
    def process_request(self, request, spider):
        ua = random.choice(AGENTS)
        if ua:
            request.headers.setdefault('User-Agent', ua)
    ```
