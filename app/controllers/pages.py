from flask import Blueprint
from twilio.rest import TwilioRestClient
from config.development.APIKeys import TwilioAccount, TwilioToken

blueprint = Blueprint('pages', __name__)
account_sid = TwilioAccount
auth_token  = TwilioToken

################
#### routes ####
################

@blueprint.route('/')
def home():
  return 'Hello World!'


@blueprint.route('/about')
def about():
  # Your Account Sid and Auth Token from twilio.com/user/account
  client = TwilioRestClient(account_sid, auth_token)

  message = client.messages.create(body="Cal Hacks Baby",
      to="+13032500788",    # Replace with your phone number
      from_="+17206135689") # Replace with your Twilio number
  return message.sid
