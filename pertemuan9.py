# SLIDE 11
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edges_from([('A', 'B'), ('A', 'D'), ('B', 'C'), ('C', 'D'),('E','F'),('E','D'),('A','C'),('F','B')])
nx.draw(G, with_labels=True)
plt.show()
