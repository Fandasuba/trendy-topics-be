from flask import Blueprint, request, jsonify
from models.trends_model import TrendsModel

trends_bp = Blueprint('trends', __name__)
trends_model = TrendsModel()

@trends_bp.route('/trending', methods=['POST'])
def get_trending():
    country = request.form.get('region', 'united_states') # For my own memory. This is like the Express method of req.body. Rather than listening for an HTTPS request, it instead targets the form that was sumbmitted from the front end.
    trending_list = trends_model.fetch_trending_searches(country)
    return jsonify({"trending": trending_list})