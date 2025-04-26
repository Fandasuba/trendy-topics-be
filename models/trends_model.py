from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from trends.trends.spiders.trends_spider import TrendsSpider
import asyncio

class TrendsModel:
    def fetch_trends(self, params):
        shared_data = []
        runner = CrawlerRunner()

        @defer.inlineCallbacks
        def crawl():
            yield runner.crawl(TrendsSpider, shared_data=shared_data, params=params)
            reactor.stop()
            print("Debug: Shared data after crawling:", shared_data)

        crawl()
        reactor.run()  # Block until the crawling is finished
        return shared_data
    
    # async def run_spider(self, params):
    #     """
    #     Run the Scrapy spider and return the scraped data.
    #     """
    #     # @defer.inlineCallbacks
    #     # def _crawl():
    #     #     """
    #     #     Helper function to handle the Twisted Deferred mechanism.
    #     #     """
    #     #     results = []
            
    #     #     # Create a custom Spider class with overridden start_requests
    #     #     class CustomTrendsSpider(TrendsSpider):
    #     #         def __init__(self, *args, **kwargs):
    #     #             super().__init__(*args, **kwargs)
    #     #             self.custom_params = params
                
    #     #         def start_requests(self):
    #     #             yield from super().start_requests(self.custom_params)

    #     #         def parse(self, response):
    #     #             trends_data = super().parse(response)
    #     #             results.extend(trends_data)  # Store the scraped data

    #     #     # Run the spider
    #     #     yield self.crawler_runner.crawl(CustomTrendsSpider)
    #     #     reactor.stop()  # Stop the reactor when done
    #     #     defer.returnValue(results)

    #     # Run the Twisted reactor in a thread
    #     return await asyncio.to_thread(lambda: reactor.run())