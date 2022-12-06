import mongoengine as db
from datetime import datetime


class User(db.Document):
    email = db.StringField(required=True,unique=True)
    password = db.StringField(required=True)
    firstName = db.StringField()
    lastName = db.StringField()
    updatedAt = db.DateTimeField(default=datetime.utcnow)
    createdAt = db.DateTimeField(default=datetime.utcnow)