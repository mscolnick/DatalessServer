from app.controllers.database import db

INBOUND = 'inbound'
OUTBOUND = 'outbound'

class Message(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  body = db.Column(db.String(1024))
  to_phone_number = db.Column(db.String(16))
  from_phone_number = db.Column(db.String(16))
  direction = db.Column(db.String(16))
  dateSent = db.Column(db.String(32))

  def __init__(self, body, to_phone_number, from_phone_number, direction, dateSent):
    self.body = body
    self.to_phone_number = to_phone_number
    self.from_phone_number = from_phone_number
    self.direction = direction
    self.dateSent = dateSent

  def __repr__(self):
    return '<Message %r>' % self.body
