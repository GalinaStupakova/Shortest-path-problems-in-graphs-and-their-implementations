import matplotlib.pyplot as plt
import pandas as pd

import scipy as sp
import random
import networkx as nx


n = 10000 
m = 499950 
G = nx.gnm_random_graph(n, m, directed=False)

# Сохраняем только пары вершин (без веса)
nx.write_edgelist(G, "graph_with_4950vertexbd.txt", data=False)
