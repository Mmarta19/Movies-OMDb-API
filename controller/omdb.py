import requests
from app import config

OMDB_URL = config.OMDB_API_URL + "?apikey=" + config.OMDB_KEY


def do_OMDB_request(movie_name):
    try:
        retval = requests.get(OMDB_URL+"&t="+movie_name)
        return retval.json(), retval.status_code
    except requests.exceptions.ConnectionError:
        return '', 'ConnectionError'
