import scrapy

class mirror_url_spider(scrapy.Spider):
    name = 'mirror_url_spider'
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

class guardian_url_spider(scrapy.Spider):
    name = 'guardian_url_spider'
    start_urls = ['https://www.theguardian.com/world/monkeypox'
                ]
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"

    def parse(self, response):

        panels = response.css('section[id]')

        for url in set(panels.css('a[data-link-name=article]::attr(href)').getall()):
            yield{
                'url': url
            }

        current_page_no = response.css('span.button.button--small.button--tertiary.pagination__action.is-active::text').get()
        next_page_no = str(int(current_page_no) + 1)
        next_page_link = response.css("a[data-page='" + next_page_no + "']::attr(href)").get()

        if next_page_link is not None:
           yield response.follow(next_page_link, callback=self.parse)

class bbc_url_spider(scrapy.Spider):
    name = 'bbc_url_spider'
    start_urls = ['https://www.bbc.com/news/topics/c3np65e0jq4t'
                ]
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"

    def parse(self, response):

        for url in set(response.css('a.ssrcss-1j8v9o5-PromoLink.e1f5wbog0::attr(href)').getall()):
            yield{
                'url': 'https://www.bbc.com' + url
            }

        next_button = response.xpath('.//div[contains(@class,"e1b2sq420")]')[-1]
        next_page_link = next_button.css('a::attr(href)').get()

        if next_page_link is not None:
           yield response.follow('https://www.bbc.co.uk/news/topics/c3np65e0jq4t' + next_page_link, callback=self.parse)

class sun_url_spider(scrapy.Spider):
    name = 'sun_url_spider'
    start_urls = ['https://www.thesun.co.uk/topic/monkeypox/'
                ]
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"

    def parse(self, response):

        for url in set(response.css('a.teaser-anchor::attr(href)').getall()):
            yield{
                'url': url
            }

        next_page_link = response.css('a.pagination-next::attr(href)').get()

        if next_page_link is not None:
           yield response.follow(next_page_link, callback=self.parse)

class metro_url_spider(scrapy.Spider):
    name = 'metro_url_spider'
    start_urls = ['https://metro.co.uk/tag/monkeypox/'
                ]
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"

    def parse(self, response):

        articles = response.css('h3.nf-title') +  response.css('h3.metro__post__title')

        for selector in articles:
            for url in set(selector.css('a::attr(href)').getall()):
                yield{
                    'url': url
                }

        next_page_link = response.css('a.nextpostslink::attr(href)').get()

        if next_page_link is not None:
           yield response.follow(next_page_link, callback=self.parse)

class telegraph_url_spider(scrapy.Spider):
    name = 'telegraph_url_spider'
    start_urls = ['https://www.telegraph.co.uk/monkeypox/'
                ]
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"

    def parse(self, response):

        article_list = response.css('section.article-list') 

        for url in set(article_list.css('a.list-headline__link.u-clickable-area__link::attr(href)').getall() ):
            yield{
                'url': 'https://www.telegraph.co.uk' + url
            }

        next_page_link = 'https://www.telegraph.co.uk' + response.css('a.pagination__link.pagination__link--next::attr(href)').get()

        if next_page_link is not None:
           yield response.follow(next_page_link, callback=self.parse)

class mail_url_spider(scrapy.Spider):
    name = 'mail_url_spider'
    start_urls = ['https://www.dailymail.co.uk/health/monkeypox/index.html'
                ]
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"

    def parse(self, response):

        large_article = response.css('div.article.article-large.cleared')

        yield{
                'url': large_article.css('a::attr(href)').getall()[0]
            }
        
        small_articles = response.css('div.article.article-small.articletext-right')

        for url in set(small_articles.css('a[itemprop="url"]::attr(href)').getall()):
            yield{
                'url': url
            }

class standard_url_spider(scrapy.Spider):
    name = 'standard_url_spider'
    start_urls = ['https://www.standard.co.uk/topic/monkeypox'
                ]
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"

    def parse(self, response):

        for url in set(response.css('a.title::attr(href)').getall()):
            yield{
                'url': 'https://www.standard.co.uk' + url
            }
