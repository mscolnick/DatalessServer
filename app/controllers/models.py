from app.controllers.database import db

class Message(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  body = db.Column(db.String(1024))
  reciever = db.Column(db.String(16))

  def __init__(self, body, reciever):
    self.body = body
    self.reciever = reciever

  def __repr__(self):
    return '<Message %r>' % self.body
