def add_directed_edge(graph, source, destination):
    graph[source].append(destination)


def add_undirected_edge(graph, source, destination):
    add_directed_edge(graph, source, destination)
    add_directed_edge(graph, destination, source)


def add_node(graph, node):
    graph[node] = []


def print_graph(graph):
    for node in graph:
        print(node, '->', graph[node])


def find_most_popular_friends(graph):
    largest_friendship_count = 0
    for node in graph:
        if len(graph[node]) > largest_friendship_count:
            largest_friendship_count = len(graph[node])

    largest_friends_list = []
    for node in graph:
        if len(graph[node]) == largest_friendship_count:
            largest_friends_list.append(node)
    return largest_friends_list


if __name__ == '__main__':
    friends = {
        'Alice': ['Bob', 'Diane', 'Fred'],
        'Bob': ['Alice', 'Cathy', 'Diane'],
        'Cathy': ['Alice', 'Diane'],
        'Diane': ['Alice', 'Fred'], 'Fred': []
    }

    add_directed_edge(friends, 'Fred', 'Cathy')
    print(friends)

    add_node(friends, 'Ginger')
    add_undirected_edge(friends, 'Ginger', 'Fred')
    print(friends)

    print_graph(friends)

    print(find_most_popular_friends(friends)) 
    # ['Alice', 'Bob']
    # O(n)
    # n*(n-1) because everytime you add a node you're adding n number of edges minus the node you've just added as it would connect to itself