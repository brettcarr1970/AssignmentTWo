import cProfile

from pythonds.basic import Queue, Deque
from pythonds.graphs import Graph
import networkx as nx
import numpy as np, random


class PrimTWo:
    def __init__(self):
        self.lines = []
        self.spe = [[], []]
        self.x = 0
        self.f = 0




        # with open("content/C_10_90.mis", encoding='UTF-8') as f:
        #     sizes = f.readline()
        #     sp =  sizes.split(" ")
        #     # print(sp)
        #     amt_node = int(sp[2])
        #     # print(amt_node)
        #     amt_edges = int(sp[3])
        #     next(f)
        #     self.lines = f.readlines()
        #     f.close()
        # for i in self.lines:
        #     x = i[:- 1].split(' ', 3)
        #     self.spe[0].append(x[1])
        #     self.spe[1].append(x[2])
        # self.g = Graph()
        # for i in range(int(amt_node)):
        #     self.g.addVertex(i)
        #     self.g.addEdge((int(self.spe[1][i])), int(self.spe[0][i]))
        # self.matrix = [[0 for x in range(amt_node)] for z in range(amt_node)]
        #
        # print(self.matrix)
        # for v in self.g:
        #     print(v)
        #     for w in v.getConnections():
        #         weight = (int(v.getId()) + int(w.getId())) % 200 + 1
        #         print("weight %s" % weight)
        #         print("v.id %s" %v.getId())
        #         print("w.id %s"  %w.getId())
        #         # print("(  %s  ,  %s  , %s )" % v.getId(), w.getId(), weight)
        #         print('-----------------------------------------------------------')
        #
        #         l = int(v.getId())
        #         h = w.getId()
        #         print(int(v.getId()))
        #         print(w.getId())
        #         self.matrix[l][h] = weight

    def bfs(self, start):
        # start.setDistance(0)
        start.setPred(None)
        vertQueue = Queue()
        vertQueue.enqueue(start)
        while vertQueue.size() > 0:
            currentVert = vertQueue.dequeue()
            for nbr in currentVert.getConnections():
                # print(nbr)
                if nbr.getColor() == 'white':
                    nbr.setColor('gray')
                    nbr.setDistance(currentVert.getDistance() + 1)
                    nbr.setPred(currentVert)
                    vertQueue.enqueue(nbr)
            currentVert.setColor('black')

    def traverse(self, y):
        x = y
        while x.getPred():
            print(x.getId())
            x = x.getPred()
        print(x.getId())

    def prim2(self, g, w, s, n):
        vt = []
        et = []
        t = (vt,et)
        test_weight = []
        edges = [0] * n
        edge_weight = [0] * n
        visited = [False] * n
        for j in range(1, n):
            edge_weight[j] = w[s][j]
            edges[j] = s
            visited[j] = False
        edge_weight[s] = 0
        visited[s] = True
        # print(visited)
        i = 0
        test_weight = edge_weight

        while len(test_weight) > 0:
            if i > 0:
                k,index = min((b,a) for a,b in enumerate(w[i]) if b>0)
                # print("%s %s" % (k,index))
                # self.ww = index
                et.append((i, index))
            k = min(test_weight)
            rm = int(test_weight.index(k))
            del test_weight[rm]
            visited[i] = True
            self.x = k
            if k not in test_weight :
                # et.append((k, edges[self.ww]))
                vt.append(k)
            i += 1

        j = 0
        for j in visited:
            if visited[j] == False and w[k][j] < edge_weight[j]:
                edge_weight[j] = w[k][j]
                edges[j] = k
        print(t)

        print(visited)