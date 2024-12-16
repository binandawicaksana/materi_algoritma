# SLIDE 11
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
# G.add_edges_from([('A', 'B'), ('A', 'D'), ('B', 'C'), ('C', 'D')])
G.add_edges_from([('Bogor', 'Depok'), ('Depok', 'Tangerang'), ('Tangerang', 'Bekasi'), ('Bekasi', 'Bandung'),('Bogor', 'Puncak'),('Puncak','Cianjur'),('Cianjur','Padalarang'),('Padalarang','Bandung')])
nx.draw(G, with_labels=True)
plt.show()
