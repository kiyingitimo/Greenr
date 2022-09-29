import graphdb
import random
from datetime import datetime as dt
chars = "1234567890QWERTYUIOPASDFGHJKLZXCVBNM"
class Post:
    def __init__(self):
        self.db = graphdb.GraphDB.getInstance()
    @staticmethod
    def generateName():
        p = ""
        for _ in range(6):
            p += random.choice(chars)
        return p
    def newPost(self,email,content,room):
        global CODE
        while True:
            try:
                code = "PST-"+Post.generateName()
                self.db.newNode({
                    "images":"",
                    "likes":"0",
                    "shares":"0",
                    "postdt":str(dt.date(dt.now())),
                    "tags":"",
                    "id":code,
                    "type":"post"
                    "content":content
                })
                break
            except graphdb.IntergrityError:
                continue
        self.db.addRelation(code,email,"author")
        self.db.addRelation(code,room,"owner")
        return {
                    "images":"",
                    "likes":"0",
                    "shares":"0",
                    "postdt":str(dt.date(dt.now())),
                    "tags":"",
                    "id":code,
                    "type":"post",
                    "content":content
                }
    def like(self,email,code):
        self.addRelation(code,email,"like")
        self.db.updateNode(code,"likes",len(self.db.getNodesOfLink(email,"like")))
    def share(self,email,code):
        self.addRelation(email,code,"share")
        self.db.updateNode(code,"shares",len(self.db.getNodesOfLink(email,"share")))
    def getRandomPost(self):
        data = self.db.getRandomNodeOfType("post")
        if data:
            return data
        else:
            return {}

