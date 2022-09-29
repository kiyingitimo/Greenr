import graphdb
from datetime import datetime as dt
import random
chars = "1234567890QWERTYUIOPASDFGHJKLZXCVBNM"
class Room:
    def __init__(self):
        self.db = graphdb.GraphDB.getInstance()
    def newRoom(self,name,email):
        self.db.newNode({
            "photo":"",
            "id":name,
            "likes":"0",
            "tags":"",
            "estdate":dt.date(dt.now()),
            "type":"room"
        })
        self.db.addRelation(name,email,"admin")
        return name
    def delRoom(self,code):
        self.db.delNode(code)
    def getRoom(self,code):
        return self.getNode(code)

r = Room()
CODE = r.newRoom("default","example@gmail.com")