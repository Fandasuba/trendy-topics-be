import logging
from pathlib import Path
import scrapy
from scrapy_splash import SplashRequest
import time

logger = logging.getLogger(__name__)

class TrendsSpider(scrapy.Spider):
    name = "trends"
    
    def __init__(self, shared_data, params, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.shared_data = shared_data
        self.params = params
        logger.info(f"TrendsSpider initialized with params: {params}")
    
    def start_requests(self):
        logger.info(f"Starting requests with params: {self.params}")
        
        geo = self.params.get('geo', 'US')
        category = self.params.get('category', '17')
        url = f"https://trends.google.com/trending?geo={geo}&category={category}"
        
        logger.info(f"Making request to URL: {url}")
        splash_args = {
            'wait': 4,
            'timeout': 90,
            'images': 0,
            'resource_timeout': 20,
        }
        
        logger.info(f"Splash args: {splash_args}")
        
        yield SplashRequest(
            url=url,
            callback=self.parse,
            args=splash_args,
            meta={'dont_redirect': True},
            errback=self.handle_error
        )
    
    def handle_error(self, failure):
        logger.error(f"Request failed: {failure}")
        self.shared_data.append({"error": str(failure)})
    
    def parse(self, response):
        logger.info(f"Response from {response.url} with {response.status} status")
        if response.status != 200:
            logger.error(f"Got non-200 response: {response.status}")
            self.shared_data.append({"error": f"Got status code {response.status}"})
            return
        
        trends_data = []
        
        trends = response.css("tr.enOdEe-wZVHld-xMbwt")
        logger.info(f"Found {len(trends)} trend elements")
        

        # Trying alternative div classses and scrpay command for scraping just in case.
        if not trends:
            logger.warning("No trends found with primary selector, trying alternatives")
            trends = response.css("div.enOdEe")
            logger.info(f"Found {len(trends)} trend elements with alternative selector")
        
        # Process trends if found
        for i, trend in enumerate(trends):
            try:
                keyword = trend.css("div.mZ3RIc::text").getall()
                related = trend.css("div.k36WW span.mUIrbf-vQzf8d::text").getall()
                time_ago = trend.css("div.A7jE4::text").get()
                
                if not keyword:
                    # Try alternative selectors
                    keyword = trend.css("div.term-text::text").getall()
                
                trends_data.append({
                    "keyword": keyword if keyword else ["Unknown"],
                    "related": related if related else [],
                    "time_ago": time_ago if time_ago else "Unknown"
                })
                logger.debug(f"Processed trend #{i+1}: {keyword}")
            except Exception as e:
                logger.error(f"Error processing trend #{i+1}: {e}")
        
        logger.info(f"Extracted {len(trends_data)} trends")
        
        # Debug there incase we found no data but got a successful response. Likely Crawler JS not working or Google has changd its Trends div names again.
        if not trends_data and response.status == 200:
            logger.warning("Got 200 response but found no trends data")
            trends_data.append({"info": "No trends found in the response"})
        
        # Sends  back data to parent model for parsing back to controller.
        self.shared_data.extend(trends_data)
        logger.info(f"Updated shared_data with {len(trends_data)} items")
        
        return trends_data