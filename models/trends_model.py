import requests
import asyncio
import aiohttp

class TrendsModel:
    def __init__(self):
        self.splash_url = "http://localhost:8050"
    
    def fetch_trends(self, params):
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
            request_data = {
                'geo': geo,
                'category': category
            }
            
            async with session.post(self.splash_url, json=request_data) as response:
                if response.status != 200:
                    error_text = await response.text()
                    raise Exception(f"Error from Scrapy Splash: {error_text}")
                
                return await response.json()