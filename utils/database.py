from mongoengine import connect
from dotenv import load_dotenv
import os
load_dotenv()

def connectToDatabase():
    connect(host=os.getenv("MONGO_HOST"), db=os.getenv("MONGO_DB"), username=os.getenv("MONGO_USER"), password=os.getenv("MONGO_PASSWORD"))