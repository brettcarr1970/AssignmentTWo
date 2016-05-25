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
        vt = [0]
        et = [0]
        t = (et)
        edges = [0] * n
        edge_weight = [0] * n
        visited = [False] * n
        for j in range(1, n):
            edge_weight[j] = w[s][j]
            edges[j] = j
            visited[j] = False

        edge_weight[s] = 0
        visited[s] = True
        # print(visited)
        i = 1
        k = 0
        # print(edge_weight)
        while i < len(visited) - 1 and visited[i]:
            # k = min(i for i in edge_weight if i > self.x)
            for e in range(1, len(w)):
                k = min(i for i in w[e] if i > 0)
                print(k)
                self.x = k
                visited[i] = True
                # print(edge_weight[i])
                print("The Index: %s"  % edge_weight.index(edge_weight[i]))
                et.append((k, edges[edge_weight.index(edge_weight[i])]))
                vt.append(k)
                i += 1
        for j in visited:
            if not i:
                if w[k][j] < edge_weight[j]:
                    edge_weight[j] = w[k][j]
                    edges[j] = k
        print(t)

        print(visited)

# g.addEdge(0, 1)
# g.addEdge(0, 5)
# g.addEdge(1, 2)
# g.addEdge(2, 3)
# g.addEdge(3, 4)
# g.addEdge(3, 5)
# g.addEdge(4, 0)
# g.addEdge(5, 4)
# g.addEdge(5, 2)
# for v in g:
#     for w in v.getConnections():
#         print("(  %s  ,  %s  )" % (v.getId(), w.ge# tId()))

# g = [1, 2, # 3, 4, 5]
# matrix = [[0, 2, 3# , 4, 5],
#           [1, 0, 3# , 4, 5],
#           [1, 2, 0# , 4, 5],
#           [1, 2, 3# , 0, 5],
#           [1, 2, 3# ,#  4, 0]]
#
# p = PrimTWo()
# p.bfs(p.g.getVertex(1))
# p.traverse(p.g.getVertex(211))
# s = ??1
# n = 5
# print(matrix)
# # print(p.matrix)
# p.prim2(p, matrix, s, n)
# # cProfile.run('p.bfs(p.g.getVertex(60))')

