import heapq
from audioop import reverse
from collections import deque


def bfs_grid(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(start, [start])])
    visited = set([start])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == goal:
            return path
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == 0 and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append(((nx, ny), path + [(nx, ny)]))
    return None


grid = [
    [0, 1, 0, 0],
    [0, 0, 0, 1],
    [1, 0, 1, 0],
    [0, 0, 0, 0],
]

path = bfs_grid(grid, (0, 0), (3, 3))
print("Grid path", path)
print("Print length:", len(path) if path else 0)


# Task 03 depth first search tree - stack
def dfs_iterative(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)

            # reversed is used ti maintain the order of neighors
            # so that left - most neighnor is visited first
            stack.extend(reversed(graph[node]))


graph = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F"],
    "D": [],
    "E": ["G"],
    "F": [],
    "G": [],
}


# task 4
def detect_cycle(graph):
    visited = set()
    rec_stack = set()

    def dfs(node):
        visited.add(node)
        rec_stack.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True

        rec_stack.remove(node)
        return False

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False


# Greedy best first search tree
def greedy_best_first(graph, start, goal, heurisitc):
    visited = set()
    pq = [(heurisitc[start], start)]
    parent = {start: None}
    while pq:
        _, nod = heapq.heappop(pq)
