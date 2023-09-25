def find_friends(social_network, source):
    queue = []
    queue.append(source)

    levels = []
    visited = []
    step = 1

    while queue:
        node = queue.pop(0)
        # print(f"Dequeue {node}")

        if node not in visited:
            visited.append(node)
            # print(f"Visiting {node}")

            level = []
            for neighbor in social_network[node]:
                if neighbor not in queue and neighbor not in visited:
                    # print(f"Enqueue {neighbor}")
                    queue.append(neighbor)
                    level.append(neighbor)
            if level:
                levels.append(level)

        step += 1
    return levels


def find_least_popular_friends(graph):
    smallest_friend_count = None
    for node in graph:
        if smallest_friend_count == None or len(graph[node]) < smallest_friend_count:
            smallest_friend_count = len(graph[node])

    smallest_friend_list = []
    for node in graph:
        if len(graph[node]) == smallest_friend_count:
            smallest_friend_list.append(node)
    return smallest_friend_list


if __name__ == "__main__":
    file = open('social_network_50.txt')
    social_network = eval(file.read())
    file.close()

    for person in find_least_popular_friends(social_network):
        print(
            f"{person} suggestions are {find_friends(social_network, person)[2:]}")
    # Ernest suggestions are [
    # ['William', 'Gary', 'Shawn', 'Andrew', 'Joe', 'Peter', 'Russell', 'Mark', 'Jerry', 'Alan', 'Frank', 'Raymond'],
    # ['Louis', 'Harold', 'Eric', 'Willie'],
    # ['Steven', 'Jonathan', 'Daniel'],
    # ['Justin', 'Chris'],
    # ['Victor', 'Stephen'],
    # ['Brandon']
    # ]
