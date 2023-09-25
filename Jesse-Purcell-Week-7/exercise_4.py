from exercise_1 import *
from exercise_2 import *
from exercise_3 import *
from pyvis.network import Network


if __name__ == '__main__':
    weighted_graph = {}
    weighted_graph['AlphaCo'] = {}
    weighted_graph['BetaCorp'] = {}
    weighted_graph['GammaInc'] = {}
    weighted_graph['DeltaLLC'] = {}
    weighted_graph['EpsilonPlc'] = {}

    weighted_graph['AlphaCo']['BetaCorp'] = 5
    weighted_graph['AlphaCo']['GammaInc'] = 7.5
    weighted_graph['AlphaCo']['EpsilonPlc'] = 5
    weighted_graph['BetaCorp']['GammaInc'] = 4.5
    weighted_graph['BetaCorp']['DeltaLLC'] = 8
    weighted_graph['GammaInc']['BetaCorp'] = 4.5
    weighted_graph['GammaInc']['DeltaLLC'] = 6
    weighted_graph['DeltaLLC']['EpsilonPlc'] = 9
    weighted_graph['EpsilonPlc']['AlphaCo'] = 14
    weighted_graph['EpsilonPlc']['GammaInc'] = 7

    for node in weighted_graph:
        costs, predecessors = compute_shortest_path(weighted_graph, node)

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
            f'A graph representing the shortest paths from {node} to all reachable companies:')
        display_graph_indented(shortest_paths)
        net = Network(directed=True)
        for predecessor in predecessors:
            net.add_node(predecessor)
        for predecessor in predecessors:
            for edge in shortest_paths[predecessor]:
                net.add_edge(predecessor, edge, label=str(costs[edge]))
        net.save_graph(f'{node}.html')
