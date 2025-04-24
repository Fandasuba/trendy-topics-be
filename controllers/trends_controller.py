from flask import request, jsonify
from models.trends_model import TrendsModel 
print("Inside controller file")

def setup_trends_routes(app):
    print(f"Setting up routes for app: {app}")
    
    @app.route('/trending', methods=['POST'])
    def get_trends():
        print("Endpoint /trending was called")
        params = request.get_json()
        print(f"Request params: {params}")
       
        if not params:
            return jsonify({"error": "No parameters provided"}), 400
       
        trends_model = TrendsModel()
       
        try:
            print("Trying to fetch trends")
            results = trends_model.fetch_trends(params)
            print(f"Results: {results}")
            return jsonify({
                "status": "success",
                "data": results
            })
           
        except Exception as e:
            print(f"Error: {str(e)}")
            return jsonify({
                "status": "error",
                "message": str(e)
            }), 500