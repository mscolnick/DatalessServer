import requests
import json

#--------------------------Data.gov Food-----------------------------------#
#get nutritional information for a food

datagov_api_key = 'jjvdbRrkoF6dCLrAvcXhOvgUPxJqEHy32wDZCuhM'

def get_ndbno(food):
  url = 'http://api.nal.usda.gov/ndb/search/?format=json&q=%s&max=1&offset=0&api_key=%s' % (food, datagov_api_key)
  return json.loads(requests.get(url).content)['list']['item'][0]['ndbno']

def get_nutritional_facts(food):
  try:
    nbdno = get_ndbno(food)
    url = 'http://api.nal.usda.gov/ndb/reports/?ndbno=%s&type=b&format=json&api_key=%s' % (nbdno, datagov_api_key)
    resp = json.loads(requests.get(url).content)['report']
    resp = resp['food']['nutrients']
    nutrients = []
    for i in resp:
      nutrients += [i['name']]
    return nutrients
  except:
    return "no food found"

# print get_nutritional_facts('bacon')
# ipy.embed()
