from pyvis.network import Network

file = open('social_network_50.txt')
graph = eval(file.read())
file.close()


net = Network(directed=True, select_menu=True, filter_menu=True)

for node in graph:
    net.add_node(node)

for node in graph:
    for edge in graph[node]:
        net.add_edge(node, edge)

net.show_buttons(filter_=['physics'])
net.repulsion(node_distance=500)
net.save_graph('social_network.html')
