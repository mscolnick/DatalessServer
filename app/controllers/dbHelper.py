from app.controllers.models import Message
from app.controllers.database import db

def addMessageToDB(body, to_phone_number, from_phone_number, direction, date):
  m = Message(body, to_phone_number, from_phone_number, direction, date)
  db.session.add(m)
  db.session.commit()
  return m.id

def getAllMessages():
  return Message.query.all()

def getMessageById(myId):
  return Message.query.filter_by(id=myId).first()
