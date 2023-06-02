#!/usr/bin/python3
import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()   # an empty undirected graph

n = 6   # number of nodes
p = 0.5 # probability for edge creation
G = nx.erdos_renyi_graph(n, p) # function to create random graph. By default it creates undirected graph
print(G.nodes)
print(G.edges)
nx.draw(G)
plt.show()