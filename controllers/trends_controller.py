from flask import request, jsonify
from models.trends_model import TrendsModel

print("Inside controller file")

trends_model = TrendsModel()

def setup_trends_routes(app):
    @app.route('/trending', methods=['POST'])
    def get_trends():
        params = request.get_json()
        
        if not params:
            return jsonify({"error": "No parameters provided"}), 400
        
        trends_model = TrendsModel()
        
        try:
            results = trends_model.fetch_trends(params)
            return jsonify({
                "status": "success",
                "data": results
            })
            
        except Exception as e:
            return jsonify({
                "status": "error",
                "message": str(e)
            }), 500


# The code below is for the old API i was using that now seems broken. Instead using Scrapy to make my own web scraping service for trends.

# def setup_trends_routes(app):
#     @app.route('/api/trending', methods=['POST'])
#     def get_trending():
#         # Check if the request has JSON data
#         if request.is_json:
#             data = request.get_json()
#             print(data)
#             country = data.get('geo', 'united_states')
#             print(f"JSON request received with country: {country}")
#         # Check if the request has form data
#         elif request.form:
#             country = request.form.get('region', 'united_states')
#             print(f"Form data request received with region: {country}")
#         else:
#             print("No data found in request")
#             country = 'united_states'  # Default fallback
        
#         print(f"Processing request for country: {country}")
        
#         # Convert region code if needed (e.g., 'US' to 'united_states')
#         if country == 'US':
#             country = 'united_states'
            
#         trending_list = trends_model.fetch_trending_searches(country)
#         return jsonify({"trending": trending_list})
