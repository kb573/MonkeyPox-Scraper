import scrapy
import json

class mirror_article_spider(scrapy.Spider):
    name = 'mirror_article_spider'

    def start_requests(self):
        
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0"}

        urls = []

        with open("mirror_urls.json", "r") as f:
            jsonlist = json.load(f)

        for i in range(len(jsonlist)):
            url = jsonlist[i]["url"]
            urls.append(url)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=headers)

    def parse(self, response):
        
        time = response.css('ul.time-info')
        article = response.css('div.article-body')

        yield{
            'title': response.css('h1.lead-content__title::text').get(),
            'author': response.css('a.publication-theme::text').get(),
            'date': time.css('li::text').get(),
            'text': ' '.join(article.css('p ::text').extract()),
            'url': response.request.url
        }

class guardian_article_spider(scrapy.Spider):
    name = 'guardian_article_spider'

    def start_requests(self):
        
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0"}

        urls = []

        with open("guardian_urls.json", "r") as f:
            jsonlist = json.load(f)

        for i in range(len(jsonlist)):
            url = jsonlist[i]["url"]
            urls.append(url)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=headers)

    def parse(self, response):
        
        title = response.css('div.dcr-1nupfq9')
        subtitle = response.css('div.dcr-zjgnrw')

        yield{
            'title': title.css('h1::text').get() ,
            'author': response.css('a[rel=author]::text').get(),
            'date': response.css('span.dcr-10i63lj::text').get(),
            'text': ' '.join(response.css('p.dcr-xry7m2::text, a[data-link-name="in body link"]::text').getall()),
            'url': response.request.url
        }

class bbc_article_spider(scrapy.Spider):
    name = 'bbc_article_spider'

    def start_requests(self):
        
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0"}

        urls = []

        with open("bbc_urls.json", "r") as f:
            jsonlist = json.load(f)

        for i in range(len(jsonlist)):
            url = jsonlist[i]["url"]
            urls.append(url)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=headers)

    def parse(self, response):
        
        author = response.css('p.ssrcss-ugte5s-Contributor.e5xb54n2') 
        article = response.css('article')

        yield{
            'title': article.css('h1[id=main-heading]::text, span[role=text]::text').get(),
            'author': author.xpath('//span/strong/text()').get() ,
            'date': response.xpath('//time[@data-testid="timestamp"]/@datetime').extract_first() ,
            'text': ' '.join(article.css('p.ssrcss-1q0x1qg-Paragraph.eq5iqo00::text, a.ssrcss-k17ofw-InlineLink.e1no5rhv0::text,  h2.ssrcss-y2fd7s-StyledHeading.e1fj1fc10::text').getall()),
            'url': response.request.url
        }

class sun_article_spider(scrapy.Spider):
    name = 'sun_article_spider'

    def start_requests(self):
        
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0"}

        urls = []

        with open("sun_urls.json", "r") as f:
            jsonlist = json.load(f)

        for i in range(len(jsonlist)):
            url = jsonlist[i]["url"]
            urls.append(url)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=headers)

    def parse(self, response):
        
        article_text = response.css('div.article__content')

        yield{
            'title': response.css('h1.article__headline::text').get(),
            'author': response.css('a.author.url.fn.article__author-link.t-p-color::text').get(),
            'date': response.css('span.article__datestamp::text').get() + response.css('span.article__timestamp::text').get(),
            'text': ' '.join(article_text.css('p::text, a::text,  h2::text').extract()),
            'url': response.request.url
        }

class metro_article_spider(scrapy.Spider):
    name = 'metro_article_spider'

    def start_requests(self):
        
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0"}

        urls = []

        with open("metro_urls.json", "r") as f:
            jsonlist = json.load(f)

        for i in range(len(jsonlist)):
            url = jsonlist[i]["url"]
            urls.append(url)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=headers)

    def parse(self, response):
        
        article_body = response.css('div.article-body')

        yield{
            'title': response.css('h1.post-title.clear::text').get(),
            'author': response.css('a.author.url.fn::text').get(),
            'date': response.css('span.post-date::text').get(),
            'text': ' '.join(article_body.css('p::text').extract()),
            'url': response.request.url
        }

class telegraph_article_spider(scrapy.Spider):
    name = 'telegraph_article_spider'

    def start_requests(self):
        
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0"}

        urls = []

        with open("telegraph_urls.json", "r") as f:
            jsonlist = json.load(f)

        for i in range(len(jsonlist)):
            url = jsonlist[i]["url"]
            urls.append(url)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=headers)

    def parse(self, response):
        
        authors = response.css('div.tpl-article__byline-date')
        article_body = response.css('div[itemprop="articleBody"]')
        article_texts = article_body.css('div.articleBodyText.section')

        yield{
            'title': response.css('h1.e-headline.u-heading-1::text').get(),
            'author': authors.css('span.e-byline__author::text').getall(),
            'date': response.css('time.e-published-date.u-meta::text').get(),
            'text': ' '.join(article_texts.css('p::text').extract()),
            'url': response.request.url
        }

class mail_article_spider(scrapy.Spider):
    name = 'mail_article_spider'

    def start_requests(self):
        
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0"}

        urls = []

        with open("mail_urls.json", "r") as f:
            jsonlist = json.load(f)

        for i in range(len(jsonlist)):
            url = jsonlist[i]["url"]
            urls.append(url)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=headers)

    def parse(self, response):
        
        article_body = response.css('div[id="js-article-text"]')
        date_time = article_body.css('span.article-timestamp.article-timestamp-published')
        article_text = article_body.css('div[itemprop="articleBody"]')

        yield{
            'title': article_body.css('h2::text').get(),
            'author': article_body.css('a.author::text').get(),
            'date': date_time.css('time::text').get(),
            'text': ' '.join(article_text.css('p::text, a::text').extract()),
            'url': response.request.url
        }

class standard_article_spider(scrapy.Spider):
    name = 'standard_article_spider'

    def start_requests(self):
        
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0"}

        urls = []

        with open("standard_urls.json", "r") as f:
            jsonlist = json.load(f)

        for i in range(len(jsonlist)):
            url = jsonlist[i]["url"]
            urls.append(url)

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=headers)

    def parse(self, response):
        
        article_body = response.css('article')
        date_time = article_body.css('div.sc-bKhNmF.llqrbS.publish-date')
        article_text = article_body.css('div[id="main"]')

        yield{
            'title': article_body.css('h1.sc-jnWwQn.byZbup::text').get() ,
            'author': article_body.css('a.ssc-enyVUO.bLyQEY::text').get(),
            'date': date_time.css('::text').get() ,
            'text': ' '.join(article_text.css('p::text, a::text,  h2::text, span::text').extract()),
            'url': response.request.url
        }