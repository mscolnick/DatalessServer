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
    # [
    #   {
    #     "group": "Proximates",
    #     "name": "Water",
    #     "nutrient_id": "255",
    #     "value": "0.25",
    #     "unit": "g"
    #   },
    #   ...
    # ]
    try:
      nbdno = self.get_ndbno(food)
      url = 'http://api.nal.usda.gov/ndb/reports/?ndbno=%s&type=b&format=json&api_key=%s' % (nbdno, self.datagov_api_key)
      resp = json.loads(requests.get(url).content)['report']['food']['nutrients']
      filtered = []
      for e in resp:
        item = {
          "group": e['group'],
          "name": e['name'],
          "name": e['name'],
          "value": e['value'],
          "unit": e['unit']
        }
        filtered.append(item)
      return json.dumps(filtered)
    except:
      return "[]"

if __name__ == '__main__':
  dgov_api = DataGovApi()
  print dgov_api.get_ingredients('bacon')
