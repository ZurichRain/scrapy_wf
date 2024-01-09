import scrapy

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('span small::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)


import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/page/1']

    def parse(self, response):
        # 处理响应，提取数据等

        # 构造下一个页面的链接
        current_page_number = int(response.url.split('/')[-1])
        next_page_number = current_page_number + 1
        next_page_url = f'http://example.com/page/{next_page_number}'

        # 判断是否还有下一页，可以是基于某些条件的判断，例如页面数上限
        if next_page_number <= MAX_PAGE:
            yield scrapy.Request(next_page_url, callback=self.parse)
