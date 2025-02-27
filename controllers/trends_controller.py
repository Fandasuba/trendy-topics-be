from flask import Blueprint, request, jsonify
from models.trends_model import TrendsModel
print("Inside controller file")
trends_bp = Blueprint('trends', __name__)
trends_model = TrendsModel()

@trends_bp.route('/trending', methods=['POST'])
def get_trending():
    data = request.get_json()  # Python's JSON parse equivalent since im sending over a json format copy.
    print(data, "Looking for data.")
    country = data.get('geo', 'united_states')
    print(country, "Looking for country data")
    trending_list = trends_model.fetch_trending_searches(country)
    return jsonify({"trending": trending_list})