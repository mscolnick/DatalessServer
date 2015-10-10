import requests
import json

#------------------------Capital One------------------------------------#
#Get balance of an account

cone_url = 'http://api.reimaginebanking.com'
cone_key = '1366093bda72bf51ff7a0449c3e7f910'

def get_accounts():
  r = requests.get('http://api.reimaginebanking.com/accounts?key='+cone_key)
  return json.loads(r.content)

def get_account(account_id):
  r = requests.get(str(cone_url) + '/accounts/' + str(account_id) + "?key=" + cone_key)
  return json.loads(r.content)

def get_balance(account_id):
  return int(get_account(account_id)["balance"])

def get_customers():
  #Returns python dictionary of customers
  r = requests.get('http://api.reimaginebanking.com/customers?key='+cone_key)
  return json.loads(r.content)

# def create_account(account_id, customer_id, payload):
#   r = requests.post(cone_url+, data=json.dumps(payload), headers={'content-type':'application/json'})
#   return r.text

# print get_accounts()
# print get_balance('560f0207f8d8770df0efa460')
# print get_customers()

# create_account(1, {
#           "type": "Savings",
#           "nickname": "Shane",
#           "rewards": 0,
#           "balance": 0})

