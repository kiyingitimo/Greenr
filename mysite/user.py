import graphdb
import hashlib
from datetime import datetime as dt
class User:
    def __init__(self):
        self.db = graphdb.GraphDB.getInstance()
    def signup(self,name,email,password):
        password = hashlib.sha512(password.encode("utf-8")).hexdigest()
        try:
            self.db.newNode({
                "id":email,
                "name":name,
                "password":password,
                "prefers":"",
                "propic":"",
                "estdate":str(dt.date(dt.now())),
                "followers":"0",
                "following":"0",
                "type":"usr"
            })
        except graphdb.IntergrityError:
            return 1
        return password
    def login(self,email,password):
        data = self.db.getNode(email)
        if not data:
            return 1
        elif data["password"] != hashlib.sha512(password.encode("utf-8")).hexdigest():
            return 0
        else:
            return data
    def getData(self,email,password):
        data = self.db.getNode(email)
        if data["password"] == password:
            return data
        else:
            return {}
    def addFollower(self,email_follower,email_followee,password):
        x = self.getData(email_followee,password)
        if x == {}:
            self.db.addRelation(email_followee,email_follower,"follow")
            self.db.updateNode(email_followee,"following",len(self.db.getNodesOfLink(email_followee,"follow")))
            return True
    def follow(self,email1,email2,password):
        self.addFollower(email2,email1,password)
u = User()
u.signup("Michael Greener","example@gmail.com","200634")