from flask import Blueprint, request, jsonify, make_response, redirect
from api.services.url_service import get_all_urls, create_url, get_url_by_id
from api.utils import generateShortUrl
from flask_cors import CORS

api_bp = Blueprint('api', __name__)
CORS(api_bp)

@api_bp.route('/api/urls', methods=['GET'])
def get_urls():
  try:
    resp = make_response(jsonify(get_all_urls()), 200)
    return resp
  except Exception as e:
    return make_response(jsonify({'message': str(e)}), 500)
  
@api_bp.route('/api/urls', methods=['POST'])
def add_url():
  try:
    data = request.get_json() 
    hash = generateShortUrl()
    if data:
        resp = make_response(jsonify(create_url(hash, data)), 201)
        return resp
  except Exception as e:
    return make_response(jsonify({'message': str(e)}), 500)
  
@api_bp.route('/api/urls/<id>', methods=['GET'])
def get_url(id):
  try:
    resp = make_response(jsonify(get_url_by_id(id)), 200)
    if not resp:
      return make_response(jsonify({'message': 'url not found'}), 404)
    return resp
  except Exception as e:
    return make_response(jsonify({'message': str(e)}), 500)
  
@api_bp.route('/<id>', methods=['GET'])
def redirect_to_url(id):
  try:
    url = get_url_by_id(id)
    if not url:
      return make_response(jsonify({'message': 'url not found'}), 404)
    return redirect(url['url'], code=302)
  except Exception as e:
    return make_response(jsonify({'message': str(e)}), 500)