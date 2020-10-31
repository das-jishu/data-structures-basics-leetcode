
# IMPLEMENTING BFS

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

def bfs(graph, start):
    if not graph:
        return
    visited = []
    queue = [start]
    while len(queue) > 0:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
        for adj in vertex.connectedTo:
            if adj not in visited:
                queue.append(adj)
    return visited

def recursiveBFS(q, visited):
    if len(q) == 0:
        return
    
    x = q.pop(0)
    if x not in visited:
        visited.append(x)
    for k in x.connectedTo:
        if k not in visited:
            q.append(k)
    recursiveBFS(q, visited)


if __name__ == "__main__":
    g = Graph()
    for i in range(1, 9):
        g.addVertex(i)

    g.addEdge(1, 2, 1)
    g.addEdge(1, 3, 1)
    g.addEdge(3, 4, 1)
    g.addEdge(4, 6, 1)
    g.addEdge(4, 5, 1)
    g.addEdge(6, 7, 1)
    g.addEdge(7, 8, 1)
    g.addEdge(5, 8, 1)

    re = bfs(g, g.getVertex(1))
    visited = []
    recursiveBFS([g.getVertex(1)], visited)
    
    print("RECURSIVE:")
    for k in visited:
        print(k.id)

    print("ITERATIVE:")
    for k in re:
        print(k.id)
        
