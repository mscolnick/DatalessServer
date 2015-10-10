from twilio.rest import TwilioRestClient
from config.development.APIKeys import Twilio
from app.controllers import dbHelper as h
import json
import twilio.twiml

#APIs
from app.apis import Bing, CapitalOne, DataGov, Here, Sigimera

HEADER_SIZE = 16

mapper = {
  "0": Bing,
  "1": CapitalOne,
  "2": DataGov,
  "3": Here,
  "4": Sigimera
}

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

    print body
    jsonMessage = json.loads(body)
    app_id = jsonMessage["app_id"]
    api_class = mapper[app_id]()
    method = jsonMessage["method"]
    assert hasattr(api_class, method), "API Class {} does not have method {}".format(api_class, method)
    params = jsonMessage["params"].values()
    respMessage = api_class.method(**params)

    resp = twilio.twiml.Response()
    resp.message(respMessage)

    return resp.sid

  def getMessages(self):
    return self.client.messages.list()
