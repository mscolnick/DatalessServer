from flask import Blueprint
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
  return " |\n ".join([m.body for m in messages])


@blueprint.route('/recieve')
def recieve(message):
  sid = mh.sendMessage(message)
  return sid
