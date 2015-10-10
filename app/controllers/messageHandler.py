from twilio.rest import TwilioRestClient
from config.development.APIKeys import Twilio
from app.controllers import dbHelper as h
import json
import textwrap

#APIs
from app.apis.Bing import BingApi
from app.apis.CapitalOne import CapitalOneApi
from app.apis.DataGov import DataGovApi
from app.apis.Here import HereApi
from app.apis.Sigimera import SigimeraApi

MAX_BODY = 1600
HEADER_SIZE = 16
MAX_CONTENT_SIZE = MAX_BODY - HEADER_SIZE

mapper = {
  "0": BingApi,
  "1": CapitalOneApi,
  "2": DataGovApi,
  "3": HereApi,
  "4": SigimeraApi
}

class MessageHandler():

  def __init__(self):
    self.client = TwilioRestClient(Twilio.Account, Twilio.Token)

  def sendMessage(self, body, to="+13032500788"):
    # "00010|012|004|1|{app='weather'}"
    # "message_id|total|fragment_id|app_id|{app='weather'}"
    h.addMessageToDB(body, to, 'sent')
    partitions = textwrap.wrap(body, MAX_CONTENT_SIZE)
    for partition in partitions:
      message = self.client.messages.create(body=partition,
        to=to,                # Replace with your phone number
        from_=Twilio.Number)  # Replace with your Twilio number
    return message.sid

  def recieveMessage(self, body, sender):
    h.addMessageToDB(body, sender, 'recieve')
    jsonMessage = json.loads(body)
    app_id = jsonMessage["app_id"]
    api_class = mapper[app_id]()
    method = jsonMessage["method"]
    assert hasattr(api_class, method), "API Class {} does not have method {}".format(api_class, method)
    params = jsonMessage["params"]
    respMessage = getattr(api_class, method)(*params)
    return self.sendMessage(str(respMessage), sender)

  def getMessages(self):
    return self.client.messages.list()
