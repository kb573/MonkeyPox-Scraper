import scrapy
import json

class comments_spider(scrapy.Spider):
    name = 'comments_spider'

    def start_requests(self):
        
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0"}

        urls = []

        with open("urls.json", "r") as f:
            jsonlist = json.load(f)

        for i in range(len(jsonlist)):
            url = jsonlist[i]["url"]
            urls.append(url)

        for url in urls:
            
            content_id = url[-8:]
            yield scrapy.Request('https://livecomments.viafoura.co/v4/livecomments/00000000-0000-4000-8000-67e599051dc3?limit=5&container_id=mirror-prod-' + content_id + '&reply_limit=2&sorted_by=newest', callback=self.parse)

    def parse(self, response):
        
        jsonob = json.loads(response.text)
        
        comment_list = []
        time_list = []
        date_list = []
        origin_list = []
        origin_title_list = []

        for content in jsonob['contents']:

            comment_list.append(content['content'])
            time_list.append(content['time'])
            date_list.append(content['date_created'])
            origin_list.append(content['origin'])
            origin_title_list.append(content['metadata']['origin_title'])

        yield{
            'comment' : comment_list,
            'time' : time_list,
            'date' : date_list,
            'origin' : origin_list,
            'origin title' :  origin_title_list
        }
