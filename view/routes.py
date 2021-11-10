from flask import request, Blueprint
import requests
import json
from app import config
import controller.omdb


routes = Blueprint('routes', __name__)


@routes.route('/movies')
def getmovies():
    req_data = request.get_json()
    if req_data == None:
        return json.dumps({"response": "invalid provided json"}), 400

    if "movie_name" not in req_data:
        return json.dumps({"response": "movie_name is required"}), 404

    resp, code = controller.omdb.do_OMDB_request(req_data["movie_name"])
    if code != 200:
        return json.dumps({"response": "error doing OMDB request", "OMDb response": resp}), 400

    return json.dumps({'response': resp}), 200
