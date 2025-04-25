import logging
from flask import request, jsonify
from models.trends_model import TrendsModel

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def setup_trends_routes(app):
    logger.info(f"Setting up routes for app: {app}")
    
    @app.route('/trending', methods=['POST'])
    def get_trends():
        logger.info("Endpoint /trending was called")
        params = request.get_json()
        logger.debug(f"Request params: {params}")
       
        if not params:
            return jsonify({"error": "No parameters provided"}), 400
        
        trends_model = TrendsModel()
       
        try:
            logger.info("Trying to fetch trends")
            results = trends_model.fetch_trends(params)
            logger.debug(f"Results: {results}")
            return jsonify({
                "status": "success",
                "data": results
            })
        except ValueError as ve:
            logger.error(f"ValueError: {str(ve)}")
            return jsonify({"status": "error", "message": "Invalid value"}), 400
        except Exception as e:
            logger.error(f"Error: {str(e)}")
            return jsonify({
                "status": "error",
                "message": str(e)
            }), 500