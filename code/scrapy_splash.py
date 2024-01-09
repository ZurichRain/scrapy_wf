### 使用splash爬取动态网页
docker pull scrapinghub/splash
docker run -p 8050:8050 scrapinghub/splash


# pip install scrapy-splash


# settings.py 中配置 

SPLASH_URL = 'http://localhost:8050'

DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
}

SPIDER_MIDDLEWARES = {
    'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}

DUPEFILTER_CLASS = 'scrapy_splash.SplashAwareDupeFilter'
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'


import scrapy
from scrapy_splash import SplashRequest

class MySpider(scrapy.Spider):
    name = 'my_spider'

    def start_requests(self):
        url = 'http://example.com'
        yield SplashRequest(url, self.parse, args={'wait': 1})

    def parse(self, response):
        # 解析响应内容

