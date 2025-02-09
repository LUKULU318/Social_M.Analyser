import os
import json
from flask import jsonify
from instagram_data import InstagramCollector

def analyze_post(request):
    # Get credentials from environment
    ig_user = os.environ.get('INSTAGRAM_USER')
    ig_pass = os.environ.get('INSTAGRAM_PASSWORD')
    
    # Initialize collector
    collector = InstagramCollector(ig_user, ig_pass)
    
    # Get post URL from request
    post_url = request.get_json().get('url')
    if not post_url:
        return jsonify({"error": "Missing post URL"}), 400
    
    # Collect data
    result = collector.get_post_data(post_url)
    return jsonify(result)
