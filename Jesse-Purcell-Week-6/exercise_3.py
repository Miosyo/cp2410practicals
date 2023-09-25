def main():
    file = open('social_network_50.txt')
    friends = eval(file.read())
    file.close()

    print(find_least_popular_friends(friends))  # Ernest


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


main()
