import numpy as np
import networkx as nx
from prim_two import PrimTWo
from graphic import DrawGraph as myg


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.matrix = []

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0
        self.matrix = []

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def make_matrix(self, g):
        self.matrix = np.matrix(g)
        return self.matrix

    def get_matrix(self):
        return self.matrix


g = Graph()
for i in range(10):
    g.addVertex(i)

g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(4, 5)
g.addEdge(5, 6)
g.addEdge(6, 7)
g.addEdge(7, 8)
g.addEdge(8, 9)
g.addEdge(9, 10)
g.addEdge(1, 3)
g.addEdge(1, 4)
g.addEdge(1, 5)
g.addEdge(1, 6)
g.addEdge(1, 7)
g.addEdge(1, 8)
g.addEdge(1, 9)
g.addEdge(1, 10)
g.addEdge(2, 5)
g.addEdge(2, 6)
g.addEdge(2, 7)
g.addEdge(2, 8)
g.addEdge(2, 9)
g.addEdge(3, 5)
g.addEdge(3, 6)
g.addEdge(3, 7)
g.addEdge(3, 8)
g.addEdge(3, 9)
g.addEdge(4, 6)
g.addEdge(4, 8)
g.addEdge(4, 9)
g.addEdge(5, 7)
g.addEdge(5, 8)
g.addEdge(5, 9)
g.addEdge(5, 10)
g.addEdge(6, 8)
g.addEdge(6, 9)
g.addEdge(6, 10)
g.addEdge(7, 9)
g.addEdge(7, 10)
g.addEdge(8, 10)

matrix = np.zeros((11, 11), dtype=np.int8)
my_list_gr = []
for v in g:
    for w in v.getConnections():
        weight = (v.getId() + w.getId()) % 200 + 1
        # print(v.getConnections())
        # print("(  %s  ,  %s  )" % (v.getId(), w.getId()))
        my_list_gr.append((v.getId(), w.getId()))
        matrix[v.getId()][w.getId()] = weight
        matrix[w.getId()][v.getId()] = weight
g = g.make_matrix(g)
print(matrix)
p = PrimTWo()
<<<<<<< HEAD
p.prim2(g, matrix, 1, 10)
=======
p.prim2(g, matrix, 1, 11)
>>>>>>> 1952c83... New changelist
# print(my_list_gr)

# gr = myg(g)
