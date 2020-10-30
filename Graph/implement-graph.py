
class Vertex(object):
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, w):
        self.connectedTo[nbr] = w

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

    def __str__(self):
        return str(self.id) + " connected to " + str([x.id for x in self.connectedTo])

class Graph(object):
    def __init__(self):
        self.vertices = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        temp = Vertex(key)
        self.vertices[key] = temp

    def getVertex(self, key):
        if key in self.vertices:
            return self.vertices[key]
        return None

    def addEdge(self, fro, to, cost=0):
        if fro not in self.vertices:
            self.addVertex(fro)
        if to not in self.vertices:
            self.addVertex(to)
        self.vertices[fro].addNeighbor(self.vertices[to], cost)

    def getVertices(self):
        return self.vertices.keys()

    def __iter__(self):
        return iter(self.vertices.values())

    def __contains__(self, n):
        return n in self.vertices

if __name__ == "__main__":
    g = Graph()
    for i in range(1, 6):
        g.addVertex(i)

    g.addEdge(2, 3, 2)

    for k in g.vertices.values():
        print(k)
        print(k.connectedTo)
