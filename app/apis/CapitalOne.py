import requests
import json

# www.reimaginebanking.com

class CapitalOneApi:
	def __init__(self):
		self.cone_url = 'http://api.reimaginebanking.com'
		self.cone_key = '1366093bda72bf51ff7a0449c3e7f910'

	def get_accounts(self):
    # Input: None
    # Output: all account information (dict)
	  r = requests.get(self.cone_url + '/accounts?key='+self.cone_key)
	  return json.loads(r.content)

	def get_account(self, account_id):
    # Input: account_id
    # Output: account information for a specific id (dict)
	  r = requests.get(str(self.cone_url) + '/accounts/' + str(account_id) + "?key=" + self.cone_key)
	  return json.loads(r.content)

	def get_balance(self, account_id):
    # Input: account_id
    # Output: balance (int)
	  return int(self.get_account(account_id)["balance"])

	def get_customers(self):
    # Input: None
	  # Output: customers (dict)
	  r = requests.get('http://api.reimaginebanking.com/customers?key=' + self.cone_key)
	  return json.loads(r.content)

if __name__ == '__main__':
	c_one_api = CapitalOneApi()
	print c_one_api.get_accounts()
	print c_one_api.get_balance('560f0207f8d8770df0efa460')
	print c_one_api.get_customers()




