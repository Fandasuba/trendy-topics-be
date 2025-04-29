import logging
from quart import request, jsonify
from models.trends_model import TrendsModel
import asyncio
import traceback

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def setup_trends_routes(app):
    logger.info(f"Setting up routes for app: {app}")
    
    @app.route('/trending', methods=['POST'])
    async def get_trends():
        logger.info("Endpoint /trending was called")
        try:
            params = await request.get_json()
            logger.debug(f"Request params: {params}")
        except Exception as e:
            logger.error(f"Error parsing JSON: {e}")
            return jsonify({"error": "Invalid JSON data"}), 400
       
        if not params:
            return jsonify({"error": "No parameters provided"}), 400
       
        trends_model = TrendsModel()
        try:
            logger.info("Trying to fetch trends asynchronously")
            
            # timeout for the controller hangs just in case.
            results = await asyncio.wait_for(
                trends_model.fetch_trends_async(params),
                timeout=90.0
            )
            
            logger.info(f"Received {len(results) if results else 0} results")
            return jsonify({
                "status": "success",
                "data": results
            })
        except asyncio.TimeoutError:
            logger.error("Request timed out after 90 seconds")
            return jsonify({
                "status": "error",
                "message": "Request timed out - the operation took too long to complete"
            }), 504
        except ValueError as ve:
            logger.error(f"ValueError: {str(ve)}")
            return jsonify({"status": "error", "message": str(ve)}), 400
        except Exception as e:
            logger.error(f"Error: {str(e)}")
            logger.error(traceback.format_exc())
            return jsonify({
                "status": "error",
                "message": str(e)
            }), 500