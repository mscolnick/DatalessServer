from twilio.rest import TwilioRestClient
from config.development.APIKeys import Twilio
from app.controllers import dbHelper as h

HEADER_SIZE = 16

class MessageHandler():

  def __init__(self):
    self.client = TwilioRestClient(Twilio.Account, Twilio.Token)

  def sendMessage(self, body, to="+13032500788"):
    # "00010|012|004|1|{app='weather'}"
    # "message_id|total|fragment_id|app_id|{app='weather'}"
    h.addMessageToDB(body, to, 'sent')
    if HEADER_SIZE + len(body) > 1600:
      raise "Body size to large, need to split up"
    message = self.client.messages.create(body=body,
      to=to,   # Replace with your phone number
      from_=Twilio.Number) # Replace with your Twilio number
    return message.sid

  def recieveMessage(self, body, sender):
    h.addMessageToDB(body, sender, 'recieve')

  def getMessages(self):
    return self.client.messages.list()
