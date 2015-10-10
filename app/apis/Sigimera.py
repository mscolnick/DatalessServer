import requests
import json

#--------------------------Sigimera-----------------------------------#
#get disaster information for the world or your location

class SigimeraApi:

  def __init__(self):
    self.sigimera_authentication_token = 'nTP7wzBk2nEos22_8DB_'

  def get_disasters_in_radius(self, lat, lon, radius=500):
    # Input: lat (int), lon(int), radius(int) in km
    # Output: [] if no disasters, list of disasters in a x radius
    try:
      url = 'http://api.sigimera.org/v1/crises?auth_token=%s&lat=%s&lon=%s&radius=%s' % (self.sigimera_authentication_token, lat, lon, str(radius))
      response = json.loads(requests.get(url).content)
      disasters = []
      for res in response:
        disasters += [res['dc_description']]
      return disasters
    except:
      return []

  def get_world_disasters(self):
    # Input: None
    # Output: [] if no disasters, list of disasters
    try:
      url = 'http://api.sigimera.org/v1/crises?auth_token=%s' % (self.sigimera_authentication_token)
      response = json.loads(requests.get(url).content)
      disasters = []
      for res in response:
        disasters += [res['dc_description']]
      return disasters
    except:
      return []

if __name__ == '__main__':
  sigimera_api = SigimeraApi()
  lat = 21.2222
  lon = -122.122
  for i in sigimera_api.get_disasters_in_radius(lat,lon,500):
    print i
    print ""

  for i in sigimera_api.get_world_disasters():
    print i
    print ""