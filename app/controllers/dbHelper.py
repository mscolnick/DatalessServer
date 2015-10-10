from app.controllers.models import Message
from app.controllers.database import db

def addMessageToDB(body, to):
  m = Message(body, to)
  db.session.add(m)
  db.session.commit()

def getAllMessages():
  return Message.query.all()

def getMessageById(myId):
  return Message.query.filter_by(id=myId).first()
