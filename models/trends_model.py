import logging
import asyncio
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from trends.trends.spiders.trends_spider import TrendsSpider
from twisted.internet import reactor, defer
from twisted.internet.task import react
import threading
import time

logger = logging.getLogger(__name__)

# Easy loggging for debugging.
reactor_running = False
reactor_thread = None

def start_reactor_in_thread():
    """Start the Twisted reactor in a separate thread if not already running"""
    global reactor_running, reactor_thread
    
    if not reactor_running:
        logger.info("Starting Twisted reactor in thread")
        
        def run_reactor():
            logger.info("Reactor thread started")
            reactor.run(installSignalHandlers=False)
            logger.info("Reactor thread stopped")
        
        reactor_thread = threading.Thread(target=run_reactor, daemon=True)
        reactor_thread.start()
        reactor_running = True
        
        # Give time for Reactor to start for debugging. Need to check if it actually start properly.
        time.sleep(1)
        logger.info("Reactor started successfully")
    else:
        logger.info("Reactor already running")


start_reactor_in_thread()

class TrendsModel:
    def __init__(self):
        logger.info("Initialising TrendsModel")
        self.settings = get_project_settings()
        
        # Add or update Scrapy settings
        self.settings.update({
            'DOWNLOAD_TIMEOUT': 60,
            'SPLASH_URL': 'http://172.19.0.2:8050/', # Keep an eye on this just in case it needs to be spash link.
            'DUPEFILTER_CLASS': 'scrapy_splash.SplashAwareDupeFilter',
            'HTTPCACHE_STORAGE': 'scrapy_splash.SplashAwareFSCacheStorage',
            'SPIDER_MIDDLEWARES': {
                'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
            },
            'DOWNLOADER_MIDDLEWARES': {
                'scrapy_splash.SplashCookiesMiddleware': 723,
                'scrapy_splash.SplashMiddleware': 725,
                'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,
            }
        })
        
        self.runner = CrawlerRunner(self.settings)
        logger.info("TrendsModel initialised with settings")
    
    async def fetch_trends_async(self, params):
        """
        Fetch trends using Scrapy/Twisted and convert to asyncio
        """
        logger.info("Starting fetch_trends_async method")
        
        
        if not reactor_running:
            start_reactor_in_thread()
        
        # Create a Future/ Basically Promise syntax from the looks of things.
        future = asyncio.Future()
        shared_data = []
        
        logger.info(f"Params being passed to spider: {params}")
        
        # Deferring is importnat for threading and async in Python. Think of it like the await when I was doing JS stuff early on.
        @defer.inlineCallbacks
        def crawl_process():
            try:
                logger.info("Starting crawl process")
                yield self.runner.crawl(TrendsSpider, shared_data=shared_data, params=params)
                logger.info("Crawl process completed")
                
                # Resolve the future with shared data
                if not future.done():
                    future.set_result(shared_data)
            except Exception as e:
                logger.error(f"Error in crawl process: {e}")
                if not future.done():
                    future.set_exception(e)
        
        # turns out threading is important. Remember this one Craig.
        reactor.callFromThread(crawl_process)
        
        # This section awaits for the crawler to complete, and offers timeouts if so.
        try:
            logger.info("Waiting for crawl to complete...")
            result = await asyncio.wait_for(future, timeout=75.0)  # 75 second timeout
            logger.info(f"Crawl completed with {len(result)} items")
            return result
        except asyncio.TimeoutError:
            logger.error("Crawl timed out after 75 seconds")
            raise TimeoutError("Web scraping operation timed out")
        except Exception as e:
            logger.error(f"Error during crawl: {e}")
            raise