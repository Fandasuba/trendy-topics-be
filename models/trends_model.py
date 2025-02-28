from pytrends.request import TrendReq

class TrendsModel:
    def __init__(self):
        self.pytrends = TrendReq(hl='en-US', tz=360)
   
    def fetch_trending_searches(self, country):
        print(f"Fetching trending searches for country: {country}")
        
        try:
            trending_df = self.pytrends.trending_searches(pn=country)
            trending_list = trending_df[0].tolist()
            print(trending_list)
            return trending_list
        except Exception as e:
            # Log the error
            print(f"Error fetching trending searches for {country}: {str(e)}")
            # Return empty list instead of crashing
            return []