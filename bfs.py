from collections import deque

# Function for Breadth-First Search (BFS)
def bfs_search(graph, start, target):
    visited = set()
    queue = deque()

    visited.add(start)
    queue.append(start)

    while queue:
        node = queue.popleft()

        if node == target:
            print("Target Found:", node)
            return

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

    print("Target Not Found")


# Graph Representation
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}


# Main Program
if __name__ == "__main__":
    bfs_search(graph, 'A', 'E')
