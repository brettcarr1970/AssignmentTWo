from pythonds.basic import Queue
from pythonds.graphs import Graph, Vertex, PriorityQueue
import sys


class SearchTrees:

    def __init__(self):
        self.d = {}
        self.g = Graph()
        self.ve = Vertex
        self.lines = []
        self.spe = [[], []]
        self.x = 0

        with open("content/C_10_50.mis", encoding='UTF-8') as f:
            sizes = f.readline()
            sp =  sizes.split(" ")
            # print(sp)
            amt_node = int(sp[2])
            # print(amt_node)
            amt_edges = int(sp[3])
            next(f)
            self.lines = f.readlines()
            f.close()
        for i in self.lines:
            x = i[:- 1].split(' ', 3)
            self.spe[0].append(x[1])
            self.spe[1].append(x[2])
        # self.g = Graph()
        for i in range(int(amt_node)):
            self.g.addVertex(i)
            self.g.addEdge((int(self.spe[1][i])), int(self.spe[0][i]))


    def build_graph(self, wordFile):
        self.d = {}
        self.g = Graph()
        wfile = open(wordFile, 'r')
        # create buckets of words that differ by one letter
        for line in wfile:
            word = line[: - 1]
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i + 1:]
                if bucket in self.d:
                    self.d[bucket].append(word)
                else:
                    self.d[bucket] = [word]
                    # add vertices and edges for words in the same bucket
        for bucket in self.d.keys():
            for word1 in self.d[bucket]:
                for word2 in self.d[bucket]:
                    if word1 != word2:
                        self.g.addEdge(word1, word2)
        return self.g

    def check_graph(self, g):
        for v in g:
            for w in v.getConnections():
                print("(  %s  ,  %s  )" % (v.getId(), w.getId()))

    def bfs(self, g, start):
        start.setDistance(0)
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

    def prim(self,  g, start):
        pq = PriorityQueue()
        for v in g:
            print(v)
            v.setDistance(sys.maxsize)
            v.setPred(None)
        start.setDistance(0)
        pq.buildHeap([(v.getDistance(), v) for v in g])
        while not pq.isEmpty():
            currentVert = pq.delMin()
            for nextVert in currentVert.getConnections():
                # print(nextVert)
                newCost = currentVert.getWeight(nextVert)
                if nextVert in pq and newCost < nextVert.getDistance():
                    nextVert.setPred(currentVert)
                    nextVert.setDistance(newCost)
                    pq.decreaseKey(nextVert, newCost)







search_tree = SearchTrees()
# se_graph = search_tree.build_graph("content/words3.txt")
# search_tree.check_graph(se_graph)
# search_tree.bfs(se_graph, se_graph.getVertex('SAIL'))
search_tree.traverse(search_tree.g.getVertex(5))
search_tree.prim(search_tree.g, search_tree.g.getVertex(5))