from flask import Blueprint, request, render_template
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

@blueprint.route('/send/<number>/<message>')
def send(number, message, app_id=0):
  sid = mh.sendMessage(message, number, app_id)
  return sid

@blueprint.route('/messages')
def messages():
  messages = h.getAllMessages()
  return render_template('messages.html', messages=messages)

@blueprint.route('/recieve', methods=['POST'])
def recieve():
  if request.method == 'POST':
    sender = str(request.values.get("From"))
    body = str(request.values.get("Body"))
    date = str(request.values.get("DateSent"))
    return mh.recieveMessage(body, sender, date)
  return "This is a POST endpoint"
