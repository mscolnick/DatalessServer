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
  return 'Dataless Home!'

@blueprint.route('/send/<message>')
def send(message):
  sid = mh.sendMessage(message)
  return sid

@blueprint.route('/messages')
def messages():
  messages = h.getAllMessages()
  return " <br/> ".join(["{} {} {}".format(m.body, m.phone_number, m.direction) for m in messages])

@blueprint.route('/recieve', methods=['POST'])
def recieve():
  if request.method == 'POST':
    sender = str(request.values.get("From"))
    body = str(request.values.get("Body"))
    date = str(request.values.get("DateSent"))
    return mh.recieveMessage(body, sender, date)
  return "This is a POST endpoint"
