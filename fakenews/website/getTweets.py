import json
import requests
from requests.auth import HTTPBasicAuth

root = "https://ed54d577eed2cde2254a1fba07f6a268.eu-west-1.aws.found.io:9243/related_tweets/tweet/"
auth = requests.auth.HTTPBasicAuth("elastic", "5SMHw4qQl3oLas5tFhzyu5Jp")

def index(tweet):
  id_str = tweet['id_str']
  url = root + id_str
  s = requests.get(url, auth=auth).status_code
  # print id_str, s
  if s == 404:
    requests.put(url, auth=auth, data = json.dumps(tweet))


def getTweets(statement):
  response = requests.get(root + '_search', auth=auth, data = json.dumps({"query":{"match":{"text":statement}}}))
  res = json.loads(response.content)
  return [h["_source"] for h in res["hits"]["hits"]]