import asyncio
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from trends.trends.spiders.trends_spider import TrendsSpider
from twisted.internet.threads import deferToThread  # Correct import
from twisted.internet import defer
from twisted.internet.asyncioreactor import AsyncioSelectorReactor
from twisted.internet import asyncioreactor
from twisted.internet import defer

# Set the event loop policy to use Twisted's reactor
asyncioreactor.install()

# Install the asyncio reactor before importing any Twisted-related modules
asyncio.set_event_loop_policy(AsyncioSelectorReactor())

class TrendsModel:
    async def fetch_trends_async(self, params):
        shared_data = []

        # Initialize Scrapy's CrawlerRunner
        runner = CrawlerRunner(get_project_settings())

        # Define crawl as an async function
        async def crawl():
            # Use deferToThread from twisted.internet.threads
            # Add callback handling for the deferred result
            deferred = deferToThread(runner.crawl, TrendsSpider, shared_data=shared_data, params=params)
            result = await self._get_deferred_result(deferred)
            return result

        # Run the crawl function and wait for the result
        trends_data = await crawl()

        return trends_data

    # Helper function to handle deferred results with asyncio
    async def _get_deferred_result(self, deferred):
        loop = asyncio.get_event_loop()
        return await loop.run_in_executor(None, deferred.result)
    
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