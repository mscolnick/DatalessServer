import requests
import json

#--------------------------Sigimera-----------------------------------#
#get disaster information for the world or your location


sigimera_authentication_token = 'nTP7wzBk2nEos22_8DB_'

lat = 21.2222
lon = -122.122

def get_disasters(lat,lon):
  try:
    # url = 'http://api.sigimera.org/v1/crises?auth_token=%s&lat=%s&lon=%s&radius=500' % (sigimera_authentication_token, lat, lon)
    url = 'http://api.sigimera.org/v1/crises?auth_token=%s' % (sigimera_authentication_token)
    response = json.loads(requests.get(url).content)
    disasters = []
    for res in response:
      disasters += [res['dc_description']]
    return disasters
  except:
    return "no disasters"

# for i in get_disasters(31.777,-122.123):
#   print i
#   print ""
