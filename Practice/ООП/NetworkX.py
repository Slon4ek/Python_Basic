import networkx as nx
import matplotlib.pyplot as plt

# Создание пустого графа
graph = nx.Graph()

# Добавление вершин
graph.add_node("A")
graph.add_nodes_from(["B", "C", "D"])

# Добавление рёбер
graph.add_edge("A", "B")
graph.add_edges_from([("B", "C"), ("C", "D"), ("D", "A")])

# Получение списка вершин и рёбер
nodes = graph.nodes()
edges = graph.edges()

# Визуализация графа
nx.draw(graph, with_labels=True, node_color='lightblue', edge_color='gray')
plt.show()

# Что-то дописал
