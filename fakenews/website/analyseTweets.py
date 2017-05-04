import json
import requests

"""
return json of format { "score": ?, "problems": [?, ?] }
"""
def analyse(tweet):
    response = requests.get('http://46.101.95.25:8000/analyse?id=' + tweet['id_str'])
    body = response.content
    return json.loads(body)