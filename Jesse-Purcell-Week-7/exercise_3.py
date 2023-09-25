from exercise_1 import *
from exercise_2 import *


def display_graph_indented(graph):
    for node in graph:
        for neighbour in graph[node]:
            print(f'\t{node} --{graph[node][neighbour]}-> {neighbour}')
        print()


def compute_shortest_path(graph, starting_node):
    costs = {}
    for node in graph:
        costs[node] = float('inf')
    costs[starting_node] = 0

    predecessors = {}
    for node in graph:
        predecessors[node] = None

    unvisited = set(graph.keys())

    while True:
        node = smallest_cost_node(unvisited, costs)
        if node is None:
            break

        unvisited.remove(node)

        for neighbor in graph[node]:
            alternative_cost = costs[node] + graph[node][neighbor]

            if alternative_cost < costs[neighbor]:
                costs[neighbor] = alternative_cost
                predecessors[neighbor] = node
    return costs, predecessors


if __name__ == '__main__':
    weighted_graph = {}
    weighted_graph['New York'] = {}
    weighted_graph['Los Angeles'] = {}
    weighted_graph['Chicago'] = {}
    weighted_graph['Houston'] = {}
    weighted_graph['Phoenix'] = {}
    weighted_graph['Philadelphia'] = {}

    weighted_graph['New York']['Los Angeles'] = 27.4
    weighted_graph['New York']['Chicago'] = 7.18
    weighted_graph['Chicago']['Houston'] = 10.89
    weighted_graph['Houston']['Phoenix'] = 11.62
    weighted_graph['Phoenix']['Los Angeles'] = 3.75
    weighted_graph['Philadelphia']['New York'] = 0.95
    weighted_graph['Philadelphia']['Chicago'] = 7.59

    compute_shortest_path(weighted_graph, 'New York')

    costs, predecessors = compute_shortest_path(weighted_graph, 'New York')

    shortest_paths = construct_shortest_paths(weighted_graph, predecessors)
    print('Costs and predecessors for each node in the graph:\n')
    print('Costs:')
    for cost in costs:
        print(f'\t{cost} {costs[cost]:.02f}')
    print()
    print('Predecessors:')
    for predecessor in predecessors:
        print(f'\t{predecessor} {predecessors[predecessor]}')
    print()
    print(
        f'A graph representing the shortest paths from New York to all reachable cities:')
    display_graph_indented(shortest_paths)
