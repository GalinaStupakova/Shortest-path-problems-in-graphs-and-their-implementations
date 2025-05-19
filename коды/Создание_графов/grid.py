import networkx as nx
import random
# создаю сетку
size = int(input())
G = nx.grid_2d_graph(size, size)
# сохраняю координаты
pos = {node: (node[0], node[1]) for node in G.nodes()}  # (x, y)
#удаляю рандомные ребра
p = float(input())
# p - аналог вероятности из графа Эрдёша-Реньи
num_edges_to_remove = int(p * G.number_of_edges())
all_edges = list(G.edges())
random.shuffle(all_edges)
G.remove_edges_from(all_edges[:num_edges_to_remove])
#делаю узлы числами, а не кортежами
G = nx.convert_node_labels_to_integers(G, label_attribute="pos")
# сохраняю G как файл

nx.write_edgelist(G, "graph_with_100002vertexbd.txt", data=False)

with open("positions05.txt", "w") as f:
    for node in G.nodes():
        x, y = G.nodes[node]["pos"]
        f.write(f"{node} {x} {y}\n")
