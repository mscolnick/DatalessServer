from app.controllers.database import db

SENT = 'sent'
RECIEVED = 'recieved'

class Message(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  body = db.Column(db.String(1024))
  phone_number = db.Column(db.String(16))
  direction = db.Column(db.String(16))

  def __init__(self, body, phone_number, direction):
    self.body = body
    self.phone_number = phone_number
    self.direction = direction

  def __repr__(self):
    return '<Message %r>' % self.body
