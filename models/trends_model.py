from pytrends.request import TrendReq

class TrendsModel:
    def __init__(self):
        self.pytrends = TrendReq(hl='en-US', tz=360)
    
    def fetch_trending_searches(self, country):
        print(f"Fetching trending searches for country: {country}")  # Debug log to check the country
        trending_df = self.pytrends.trending_searches(pn=country)
        trending_list = trending_df[0].tolist()
        return trending_list