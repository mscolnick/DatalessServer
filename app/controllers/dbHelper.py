from app.controllers.models import Message
from app.controllers.database import db

def addMessageToDB(body, phone_number, direction):
  m = Message(body, phone_number, direction)
  db.session.add(m)
  db.session.commit()

def getAllMessages():
  return Message.query.all()

def getMessageById(myId):
  return Message.query.filter_by(id=myId).first()
