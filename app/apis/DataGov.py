import requests
import json

#http://ndb.nal.usda.gov/ndb/api/doc
class DataGovApi:
  def __init__(self):
    self.datagov_api_key = 'jjvdbRrkoF6dCLrAvcXhOvgUPxJqEHy32wDZCuhM'

  def get_ndbno(self, food):
    # Input: food (string)
    # Output: ndbno id (string) 
    url = 'http://api.nal.usda.gov/ndb/search/?format=json&q=%s&max=1&offset=0&api_key=%s' % (food, self.datagov_api_key)
    return json.loads(requests.get(url).content)['list']['item'][0]['ndbno']

  def get_ingredients(self, food):
    # Input: food (string)
    # Output: [] if no food found, otherwise list of Ingredients (list)
    try:
      nbdno = self.get_ndbno(food)
      url = 'http://api.nal.usda.gov/ndb/reports/?ndbno=%s&type=b&format=json&api_key=%s' % (nbdno, self.datagov_api_key)
      resp = json.loads(requests.get(url).content)['report']
      resp = resp['food']['nutrients']
      nutrients = []
      for i in resp:
        nutrients += [i['name']]
      return nutrients
    except:
      return []

if __name__ == '__main__':
  dgov_api = DataGovApi()
  print dgov_api.get_ingredients('bacon')