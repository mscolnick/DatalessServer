import requests

# www.reimaginebanking.com

class CapitalOneApi:

  def __init__(self):
    self.cone_url = 'http://api.reimaginebanking.com'
    self.cone_key = '1366093bda72bf51ff7a0449c3e7f910'

  def get_accounts(self):
    # Input: None
    # Output: all account information (list of jsons)
    # [
    #   {
    #     "rewards": 11870,
    #     "customer_id": "560f0205f8d8770df0ef99da",
    #     "type": "Credit Card",
    #     "_id": "560f0207f8d8770df0efa460",
    #     "balance": 17181,
    #     "nickname": "Gerhardt's Account"
    #   },
    #   ...
    # ]
    r = requests.get(self.cone_url + '/accounts?key='+self.cone_key)
    return r.content

  def get_account(self, account_id):
    # Input: account_id
    # Output: account information for a specific id (dict)
    # {
    #   "rewards": 11870,
    #   "customer_id": "560f0205f8d8770df0ef99da",
    #   "type": "Credit Card",
    #   "_id": "560f0207f8d8770df0efa460",
    #   "balance": 17181,
    #   "nickname": "Gerhardts Account"
    # }
    assert account_id != ''
    r = requests.get(str(self.cone_url) + '/accounts/' + str(account_id) + "?key=" + self.cone_key)
    return r.content

  def get_customers(self):
    # Input: None
    # Output: customers (dict)
    # [
    #   {
    #     "last_name": "OReilly",
    #     "first_name": "Skylar",
    #     "_id": "560f0205f8d8770df0ef99da",
    #     "address": {
    #       "city": "Swanton",
    #       "street_name": "Coopers Lane",
    #       "zip": "21561",
    #       "state": "Maryland",
    #       "street_number": "574"
    #     }
    #   },
    #   ...
    # ]
    r = requests.get('http://api.reimaginebanking.com/customers?key=' + self.cone_key)
    return r.content

if __name__ == '__main__':
  c_one_api = CapitalOneApi()
  print c_one_api.get_accounts()
  print c_one_api.get_account('560f0207f8d8770df0efa460')
  print c_one_api.get_customers()
