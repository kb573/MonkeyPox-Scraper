import scrapy

class url_spider(scrapy.Spider):
    name = 'url_spider'
    start_urls = ['https://www.mirror.co.uk/all-about/monkeypox'
                ]
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"

    def parse(self, response):
        for article in response.css('article'):
            yield{
                'url': article.css('::attr(href)').get()
            }

        page_bar = response.css('div.pagination')
        next_page_button = page_bar.css('li.next')
        next_page_link = next_page_button.css('a::attr(href)').get()

        if next_page_link is not None:
            yield response.follow(next_page_link, callback=self.parse)