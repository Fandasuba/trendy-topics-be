import requests
import asyncio
import aiohttp
import os

class TrendsModel:
    def __init__(self):
        self.splash_url = "http://splash:8050/render.json"
        print(f"Splash URL set to: {self.splash_url}")
    
    def fetch_trends(self, params):
        print(f"--------> Here are the self and param variables: {self}, {params}")
        print("in fetch trends function of the model.")
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            return loop.run_until_complete(self._async_fetch_trends(params))
        finally:
            loop.close()
    
    async def _async_fetch_trends(self, params):
        """
        Asynchronously fetch trends from Scrapy Splash
        """
        async with aiohttp.ClientSession() as session:
            geo = params.get('geo', 'US')
            category = params.get('category', '17')
            # The URL that we want to scrape
            url = f"https://trends.google.com/trending?geo={geo}&category={category}"
            
            request_data = {
                'url': url,  # Include the URL parameter
                'geo': geo,
                'category': category
            }

            splash_endpoint = f"{self.splash_url}"
            print(f"Connecting to Splash at URL: {splash_endpoint}")
            
            async with session.post(splash_endpoint, json=request_data) as response:
                if response.status != 200:
                    error_text = await response.text()
                    raise Exception(f"Error from Scrapy Splash: {error_text}")
                
                return await response.json()