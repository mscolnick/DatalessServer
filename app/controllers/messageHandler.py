from twilio.rest import TwilioRestClient
from config.development.APIKeys import Twilio
from app.controllers import dbHelper as h
import json
import textwrap
from app.utils import cleanString, fix_number
import time

#APIs
from app.apis.Bing import BingApi
from app.apis.CapitalOne import CapitalOneApi
from app.apis.DataGov import DataGovApi
from app.apis.Here import HereApi
from app.apis.Sigimera import SigimeraApi
from app.apis.Times import TimesApi
from app.apis.Wikipedia import WikipediaApi

MAX_BODY = 1000
HEADER_SIZE = 14
MAX_CONTENT_SIZE = MAX_BODY - HEADER_SIZE

mapper = {
  "0": BingApi,
  "1": CapitalOneApi,
  "2": DataGovApi,
  "3": HereApi,
  "4": SigimeraApi,
  "5": TimesApi,
  "6": WikipediaApi
}

class MessageHandler():

  def __init__(self):
    self.client = TwilioRestClient(Twilio.Account, Twilio.Token)

  def sendMessage(self, body, to_number, app_id):
    # "00010|012|004|1|{app='weather'}"
    # "message_id|total|fragment_id|app_id|{app='weather'}"
    unique_id = h.addMessageToDB(body, to_number, Twilio.Number, 'outboud', time.strftime("%H:%M:%S"))
    partitions = textwrap.wrap(body, MAX_CONTENT_SIZE)
    for idx, partition in enumerate(partitions):
      partition = cleanString(partition)
      uid = fix_number(unique_id, 5)
      frag_len = fix_number(len(partitions), 2)
      frag_id = fix_number(idx + 1, 2)
      app_id = fix_number(app_id, 1)
      body = "{}|{}|{}|{}|{}".format(uid, frag_len, frag_id, app_id, partition)
      message = self.client.messages.create(body=body,
        to=to_number,                # Replace with your phone number
        from_=Twilio.Number)  # Replace with your Twilio number
    return message.sid

  def recieveMessage(self, body, sender, date):
    h.addMessageToDB(body, Twilio.Number, sender, 'inbound', date)
    jsonMessage = json.loads(body)
    app_id = jsonMessage["app_id"]
    api_class = mapper[app_id]()
    method = jsonMessage["method"]
    assert hasattr(api_class, method), "API Class {} does not have method {}".format(api_class, method)
    params = jsonMessage["params"]
    respMessage = getattr(api_class, method)(*params)
    return self.sendMessage(str(respMessage), sender, app_id)

  def getMessages(self):
    return self.client.messages.list()
