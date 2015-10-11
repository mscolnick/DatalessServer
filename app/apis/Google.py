import requests
import json
import IPython as ipy

class GoogleApi:
	def __init__(self):
		self.api_key = 'AIzaSyAQOpIyo2L-6SpL3e5lylN-dnahV9MPC5I'

	def decode_address(self, address):
		# Input: address (string)
		# Output: lat, lon (int)
		uri = 'https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s' % (address, self.api_key)
		resp = json.loads(requests.get(uri).content)
		temp = resp['results'][0]['geometry']['location']
		return temp['lat'], temp['lng']

if __name__ == '__main__':
	gapi = GoogleApi()
	print gapi.decode_address('2327 warring st')