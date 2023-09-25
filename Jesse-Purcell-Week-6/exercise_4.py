from exercise_1 import *

if __name__ == '__main__':
    file = open('social_network_5.txt')
    graph = eval(file.read())
    file.close()

    print_graph(graph)

    queue = []
    queue.append('Wayne')

    levels = []
    visited = []
    step = 1

    while queue:
        node = queue.pop(0)
        print(f"Dequeue {node}")

        if node not in visited:
            visited.append(node)
            print(f"Visiting {node}")

            level = []
            for neighbor in graph[node]:
                if neighbor not in queue and neighbor not in visited:
                    print(f"Enqueue {neighbor}")
                    queue.append(neighbor)
                    level.append(neighbor)
            if level:
                levels.append(level)

        print(f"Step {step} completed. Queue: {queue} Visited: {visited}")
        step += 1
    print(f"Levels: {levels}")
