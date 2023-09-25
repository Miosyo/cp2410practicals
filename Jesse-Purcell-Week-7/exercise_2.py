from exercise_1 import *


def smallest_cost_node(nodes, costs):
    smallest_cost = float('inf')
    result = None

    for node in nodes:
        if costs[node] < smallest_cost:
            smallest_cost = costs[node]
            result = node
    return result


def construct_shortest_paths(graph, predecessors):
    shortest_paths = {}

    for node in predecessors:
        shortest_paths[node] = {}

    for node in predecessors:
        predecessor = predecessors[node]
        if predecessor is not None:
            shortest_paths[predecessor][node] = graph[predecessor][node]
    return shortest_paths


if __name__ == '__main__':
    weighted_graph = {}
    for character in 'ABCDEFG':
        weighted_graph[character] = {}

    weighted_graph['A']['B'] = 1
    weighted_graph['A']['C'] = 3
    weighted_graph['B']['C'] = 1
    weighted_graph['C']['E'] = 2
    weighted_graph['D']['F'] = 3
    weighted_graph['E']['B'] = 4
    weighted_graph['F']['E'] = 2
    weighted_graph['F']['G'] = 4

    costs = {}
    for character in 'ABCDEFG':
        costs[character] = float('inf')
    costs['A'] = 0

    predecessors = {}
    for character in 'ABCDEFG':
        predecessors[character] = None
    # Predecessor holds a record of a trail we can trace back to get the shortest path
    # The cost column is the total cost to get from the current node to the starting node

    # Test code for smallest_cost_node
    print(smallest_cost_node(['A', 'B', 'C'], {'A': 1, 'B': 2, 'C': 3}))  # A
    print(smallest_cost_node(['A', 'B', 'C'], {'A': 3, 'B': 2, 'C': 1}))  # C

    # The only difference I can see is we aren't returning what the cost actually is, we just trust that it's the smallest cost based on a list of costs

    unvisited = set(weighted_graph.keys())

    while True:
        node = smallest_cost_node(unvisited, costs)
        if node is None:
            break

        unvisited.remove(node)

        for neighbor in weighted_graph[node]:
            alternative_cost = costs[node] + weighted_graph[node][neighbor]

            if alternative_cost < costs[neighbor]:
                costs[neighbor] = alternative_cost
                predecessors[neighbor] = node

    print(costs)
    print(predecessors)

    shortest_paths = construct_shortest_paths(weighted_graph, predecessors)
    display_graph(shortest_paths)
