from mongoengine import connect

from config import settings

def connectToDatabase():
    connect(host=settings.DATABASE_URL)
