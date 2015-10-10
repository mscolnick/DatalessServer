from flask import Blueprint, request
from messageHandler import MessageHandler
from app.controllers import dbHelper as h

blueprint = Blueprint('pages', __name__)
mh = MessageHandler()

################
#### routes ####
################

@blueprint.route('/')
def home():
  return 'Dataless!'

@blueprint.route('/send/<message>')
def send(message):
  sid = mh.sendMessage(message)
  return sid

@blueprint.route('/messages')
def messages():
  # messages = mh.getMessages()
  messages = h.getAllMessages()
  return " |\n ".join([m.body + m.phone_numebr + m.direction for m in messages])

@blueprint.route('/recieve', methods=['GET', 'POST'])
def recieve(message):
  if request.method == 'POST' or request.method == 'GET':
    sender = str(request.values.get("From"))
    body = str(request.values.get("Body"))
    mh.recieveMessage(body, sender)
    return request.method + sender + body
  return "Not an endpoint"
