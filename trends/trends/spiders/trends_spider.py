from pathlib import Path
import scrapy
from scrapy_splash import SplashRequest
import json

class TrendsSpider(scrapy.Spider):
    name = "trends"

    def __init__(self, shared_data, params, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.shared_data = shared_data
        self.params = params

    def start_requests(self):
        print(f"Params at the start of the start_requests function in the crawler: {self.params}")
        print(f"Shared Data at the start of the start_requests function in the crawler: {self.shared_data}")
        geo = self.params.get('geo', 'US')
        category = self.params.get('category', '17')
        url = f"https://trends.google.com/trending?geo={geo}&category={category}"
       
        yield SplashRequest(
            url=url,
            callback=self.parse,
              args={
            'wait': 4, 
            'timeout': 90,
            'images': 0,
            'resource_timeout': 20,
        },
        meta={'dont_redirect': True},
        )

    def parse(self, response):
        self.logger.info(f"Response from {response.url} with {response.status} status.")
       
        # filename = "trends_test.html"
        # Path(filename).write_bytes(response.body)
        # self.logger.info(f"Saved response to {filename}")
       
        # Divs with class "mZ3RIc" seem to be the actual trend name that pops up.
        trends_data = []
        self.logger.info(f"Params at the start of the start_requests function: {self.params}")
        self.logger.info(f"Shared Data at the start of the start_requests function: {self.shared_data}")
        for trend in response.css("tr.enOdEe-wZVHld-xMbwt"):
            keyword = trend.css("div.mZ3RIc::text").getall()
            related = trend.css("div.k36WW span.mUIrbf-vQzf8d::text").getall()
            time_ago = trend.css("div.A7jE4::text").get()
            trends_data.append({"keyword": keyword, "related": related, "time_ago": time_ago})
        # for trend in response.css("tr.enOdEe-wZVHld-xMbwt"):
        #     keyword = trend.css("div.mZ3RIc::text").getall()
        #     related = trend.css("div.k36WW span.mUIrbf-vQzf8d::text").getall()
        #     time_ago = trend.css("div.A7jE4::text").get()
        #     trends_data.append({"keyword": keyword, "related": related, "time_ago": time_ago})
        self.logger.info(f"Printing Trends Data After the css element scraping: {trends_data}")
        self.shared_data.extend(trends_data)
        self.logger.info(f"Printing Shared_Data after extending it whithin the crawler: {self.shared_data}")