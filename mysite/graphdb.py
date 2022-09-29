# import mysql.connector as sql
INSTANCE = None
import random
class IntergrityError(Exception):
    pass
class GraphDB:
    def __init__(self):
        self.connections = []
        self.nodes = []
        # db = mysql.connect(
        #   host="greener.mysql.pythonanywhere-services.com",
        #   user="greener",
        #   password="jinjacollege1",
        #   database="greener$graphdb"
        # )
    def newNode(self,dic):
        for i in self.nodes:
            if i["id"] == dic["id"]:
                raise IntergrityError()
        self.nodes.append(dic)
    def addRelation(self,id1,id2,typ):
        if not self.nodeExists(id1):
            raise KeyError(id1)
        if not self.nodeExists(id2):
            raise KeyError(id2)
        self.connections.append((id1,id2,typ))
    def getNode(self,id1):
        for i in self.nodes:
            if i["id"] == id1:
                return i
    def delNode(self,id1):
        x = 0
        while x != len(self.nodes):
            if self.nodes[x]["id"] == id1:
                del self.nodes[x]
                self.delAllOf(id1)
                self.delAllOf(id1)
                return
            x += 1

    def delRelationOfType(self,id1,typ):
        x = 0
        while x != len(self.connections):
            if self.connections[x][2] == typ and self.connections[x][0] == id1:
                del self.connections[x]
                x -= 1
            x += 1
    def delAllOf(self,id1):
        x = 0
        while x != len(self.connections):
            if self.connections[x][0] == id1 or self.connections[x][1] == id1:
                del self.connections[x]
                x -= 1
            x += 1
    def delRelation(self,id1,id2,typ=None):
        x = 0
        while x != len(self.connections):
            if self.connections[x][0] == id1 and self.connections[x][1] and (self.connections[x][2] == typ if typ else True):
                del self.connections[x]
                x -= 1
            x += 1
    @staticmethod
    def getInstance():
        global INSTANCE
        if INSTANCE:
            return INSTANCE
        else:
            INSTANCE = GraphDB()
            return INSTANCE
    def getNodesOfLink(self,id1,typ=None):
        nodes = []
        for i in self.connections:
            if i[0] == id1 and (i[2] == typ if typ is None else True):
                nodes.append(i[1])
        return nodes
    def nodeExists(self,id1):
        for i in self.nodes:
            if i["id"] == id1:
                return True
        return False
    def updateNode(self,id1,key,val):
        x = 0
        while x != len(self.nodes):
            if self.nodes[x][id1] == id1:
                self.nodes[x][id1][key] = val
                return
            x = x + 1
    def getNodesOfType(self,typ):
        p = []
        for i in self.connections:
            if i["type"] == typ:
                p.append(i)
        return p
    def getRandomNodeOfType(self,typ):
        try:
            return random.choice(self.getNodesOfType(typ))
        except IndexError:
            return False
if __name__ == "__main__":
    db = GraphDB()
    db.newNode({
        "id":"k@g.com",
        "name":"Okoed Ray"
    })
    db.newNode({
        "id":"0",
        "content":"Something"
    })
    db.addRelation("k@g.com","0","author")
    # db.delNode("0")
    print(db.getNodesOfLink("k@g.com","author"))
    print(db.nodes)
    print(db.connections)