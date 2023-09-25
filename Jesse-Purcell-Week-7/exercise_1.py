
def display_graph(graph):
    for node in graph:
        for neighbour in graph[node]:
            print(f'{node} --{graph[node][neighbour]}-> {neighbour}')
        print()


def find_reachable_nodes(graph, node):
    reachable_nodes = set()
    queue = [node]
    while queue:
        current_node = queue.pop(0)
        reachable_nodes.add(current_node)
        for neighbor in graph[current_node]:
            if neighbor not in reachable_nodes and neighbor not in queue:
                queue.append(neighbor)
    # Remove the given node from the set of reachable nodes
    reachable_nodes.remove(node)
    return reachable_nodes


def is_part_of_cycle(graph, node):
    reachable_from_node = find_reachable_nodes(graph, node)
    for reachable_node in reachable_from_node:
        if node in find_reachable_nodes(graph, reachable_node):
            return True
    return False


if __name__ == '__main__':
    weighted_graph = {}
    for character in 'ABCDEF':
        weighted_graph[character] = {}

    weighted_graph['A']['B'] = 1
    weighted_graph['A']['C'] = 3
    weighted_graph['B']['C'] = 1
    weighted_graph['B']['D'] = 2
    weighted_graph['C']['E'] = 2
    weighted_graph['D']['F'] = 3
    weighted_graph['E']['B'] = 4
    weighted_graph['F']['E'] = 2

    display_graph(weighted_graph)
    # Two cycles
    # C->E->B
    # D->D->F->E

    weighted_graph['G'] = {}
    weighted_graph['F']['G'] = 4

    display_graph(weighted_graph)

    weighted_graph['B'].pop('D')

    display_graph(weighted_graph)
    # There is only the C->E->B cycle now
    # You can longer reach G from anything other than D or F as all other connections that go in that direction have been severed

    for node in weighted_graph:
        reachable_nodes = find_reachable_nodes(weighted_graph, node)
        print(f"{node} can reach: {reachable_nodes}")

    for node in weighted_graph:
        print(
            f'Is {node} part of a cycle: ', 'yes' if is_part_of_cycle(weighted_graph, node) else 'no')
