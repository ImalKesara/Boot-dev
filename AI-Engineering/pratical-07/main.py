# uninformed search algorithms
# BFS
from collections import deque


def bfs_shortest_path(graph, start, goal):
    # A set to store visited nodes (to avoid revisiting)
    visitied = set()

    queue = deque([(start, [start])])
    while queue:
        # remove first elemt from queue
        node, path = queue.popleft()
        if node == goal:
            # return shortest path immediately
            return path
        if node not in visitied:
            visitied.add(node)

            for neighbor in graph[node]:
                queue.append((neighbor, path + [neighbor]))

    return None


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": [],
}


result = bfs_shortest_path(graph, "A", "G")
print(result)
