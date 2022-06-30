import scrapy
import json

class article_spider(scrapy.Spider):
    name = 'article_spider'

    def start_requests(self):
        
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0"}

        urls = []

        with open("urls.json", "r") as f:
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
            'text': ' '.join(article.css('p ::text').extract())
        }

