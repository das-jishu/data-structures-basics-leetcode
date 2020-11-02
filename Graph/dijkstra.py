
# PRONOUNCED AS 'DAAIKSTRA'

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

    def disjkstra(self, src, dest):
        if dest.id not in self.vertices or src.id not in self.vertices:
            return None
        dist = {}
        for vert in self.vertices.values():
            dist[vert] = float('inf')

        dist[src] = 0
        visited = []
        prevVertex = { vertex: None for vertex in self.vertices.values() }
        while dest not in visited:
            min = float('inf')
            x = None
            for y in dist:
                if dist[y] < min and y not in visited:
                    min = dist[y]
                    x = y

            if min == float('inf'):
                break
            visited.append(x)
            for nbr in x.connectedTo:
                if nbr in visited:
                    break
                if (dist[x] + x.connectedTo[nbr]) < dist[nbr]:
                    dist[nbr] = dist[x] + x.connectedTo[nbr]
                    prevVertex[nbr] = x
            
        path, current = [], dest
        while prevVertex[current] != None:
            path.insert(0, current.id)
            current = prevVertex[current]
        path.insert(0, src.id)
        #return dist[dest]
        return path
        


if __name__ == "__main__":
    g = Graph()
    for i in range(9):
        g.addVertex(i)

    g.addEdge(0, 1, 4)
    g.addEdge(0, 7, 8)
    g.addEdge(1, 2, 8)
    g.addEdge(2, 3, 7)
    g.addEdge(1, 7, 11)
    g.addEdge(7, 8, 7)
    g.addEdge(2, 8, 2)
    g.addEdge(7, 6, 1)
    g.addEdge(8, 6, 6)
    g.addEdge(6, 5, 2)
    g.addEdge(2, 5, 4)
    g.addEdge(3, 5, 14)
    g.addEdge(5, 4, 10)
    g.addEdge(3, 4, 9)

    print(g.disjkstra(g.getVertex(0), g.getVertex(8)))
