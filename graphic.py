import networkx as nx
import matplotlib.pyplot as plt


class DrawGraph:

    def __init__(self, gra):
        self.graph = gra

    def draw_graph(self ,graph, labels=None, graph_layout='shell',
                   node_size=1600, node_color='blue', node_alpha=0.3,
                   node_text_size=12,
                   edge_color='blue', edge_alpha=0.3, edge_tickness=1,
                   edge_text_pos=0.3,
                   text_font='sans-serif'):

        # create networkx graph
        G=nx.Graph()

        # add edges
        for edge in graph:
            G.add_edge(edge[0], edge[1])

        # these are different layouts for the network you may try
        # shell seems to work best
        if graph_layout == 'spring':
            graph_pos=nx.spring_layout(G)
        elif graph_layout == 'spectral':
            graph_pos=nx.spectral_layout(G)
        elif graph_layout == 'random':
            graph_pos=nx.random_layout(G)
        else:
            graph_pos=nx.shell_layout(G)

        # draw graph
        nx.draw_networkx_nodes(G,graph_pos,node_size=node_size,
                               alpha=node_alpha, node_color=node_color)
        nx.draw_networkx_edges(G,graph_pos,width=edge_tickness,
                               alpha=edge_alpha,edge_color=edge_color)
        nx.draw_networkx_labels(G, graph_pos,font_size=node_text_size,
                                font_family=text_font)

        if labels is None:
            labels = range(len(graph))

        edge_labels = dict(zip(graph, labels))
        nx.draw_networkx_edge_labels(G, graph_pos, edge_labels=edge_labels,
                                     label_pos=edge_text_pos)

        # show graph
        plt.show()


gr = DrawGraph
# p =
graph = [(1, 3), (1, 7), (1, 5), (1, 8), (1, 10), (1, 4), (1, 9), (1, 6), (1, 2), (2, 3), (2, 7), (2, 5), (2, 8), (2, 9), (2, 6), (3, 7), (3, 5), (3, 8), (3, 4), (3, 9), (3, 6), (4, 9), (4, 6), (4, 5), (4, 8), (5, 9), (5, 6), (5, 8), (5, 7), (5, 10), (6, 9), (6, 7), (6, 8), (6, 10), (7, 9), (7, 8), (7, 10), (8, 9), (8, 10), (9, 10)]

#
# # you may name your edge labels
# labels = map(chr, range(65, 65+len(graph)))
# #draw_graph(graph, labels)
#
# # if edge labels is not specified, numeric labels (0, 1, 2...) will be used
# gr.draw_graph(gr, graph)