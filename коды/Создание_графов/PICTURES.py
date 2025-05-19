import matplotlib.pyplot as plt
import networkx as nx
import matplotlib.patches as mpatches

G = nx.Graph()  # создаём объект графа

# определяем список узлов (ID узлов)
nodes = ["s", "a", "b", "c", "l", "e", "d", "g", "t"]

# определяем список рёбер
# список кортежей, каждый из которых представляет ребро
# кортеж (id_1, id_2) означает, что узлы id_1 и id_2 соединены ребром
edges = [("s","a"), ("s","c"), ("a","b"), ("a","e"), ("b","s"), ("b","l"), ("b","c"), ("c","l"), ("c","d"), ("c","t"), ("d","e"), ("d","l"), ("d","t"), ("d","g"), ("g","t") ]
# добавляем информацию в объект графа
G.add_nodes_from(nodes)
G.add_edges_from(edges)
pos = nx.circular_layout(G)

node_colors = []
for node in G.nodes():
    if node == "s":
        node_colors.append("green")  # старт
    elif node == "t":
        node_colors.append("green")    # финиш
    elif node == "l":
        node_colors.append("gold")   # выделенная вершина
    else:
        node_colors.append("MidnightBlue")  # обычные вершины

options = {
    'node_color': node_colors,
    'node_size': 2000,          
    'width': 1,                 
    'arrowstyle': '-|>',        
    'arrowsize': 12,            
    'edge_color':'black',
    'font_size': 20,         # размер шрифта для названий вершин
    'font_color': 'white',   # цвет шрифта      # edge color
}

nx.draw(G, pos, with_labels = True, **options)
nx.draw_networkx_edge_labels(G, 
     pos,
    edge_labels={ ("s","a"):'6', ("s","c"):'4', ("a","b"):'8', ("a","e"):'10', ("b","s"):'5', ("b","l"):'5', ("b","c"):'4', ("c","l"):'4', ("c","d"):'10', ("c","t"):'11', ("d","e"):'9', ("d","l"):'8', ("d","t"):'14', ("d","g"):'13', ("g","t"):'1'
,
    },
    font_color='red'

)
start_patch = mpatches.Patch(color='none', label='s — стартовая вершина')
end_patch = mpatches.Patch(color='none', label='t — конечная вершина')
landmark_patch = mpatches.Patch(color='none', label='l - маяк')

plt.legend(handles=[start_patch, end_patch, landmark_patch],
           loc='lower left', fontsize=6.5)

plt.show()
