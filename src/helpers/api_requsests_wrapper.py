import json
import requests

def get_request(url, auth):
    response = requests.get(url = url, auth = auth)
    return response.json()

def post_request(url, auth, headers, payload, in_json):
    post_response = requests.post(url = url, headers = headers, auth = auth, data = json.data)
    if in_json is True:
        return post_response.json()
    return post_response