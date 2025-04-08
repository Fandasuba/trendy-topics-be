from pathlib import Path

import scrapy

geo = "GB"
category = "17"
hours = "24"

class TrendsSpider(scrapy.Spider):
    name = "trends"
    start_urls = [
        "https://trends.google.com/trending?geo={geo}&category={category}&hours={hours}",
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        Path(filename).write_bytes(response.body)