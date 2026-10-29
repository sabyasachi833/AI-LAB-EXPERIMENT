
import heapq

# Graph Representation with Edge Costs
graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('A', 2), ('D', 3)],
    'C': [('A', 4), ('D', 1)],
    'D': [('B', 3), ('C', 1), ('E', 2)],
    'E': [('D', 2)]
}

# Heuristic Values h(n) towards Goal 'E'
heuristic = {
    'A': 6,
    'B': 5,
    'C': 3,
    'D': 2,
    'E': 0
}


# A* Search Algorithm
def a_star(graph, heuristic, start, goal):
    """
    A* Search Algorithm using f(n) = g(n) + h(n)
    g(n) = exact cost from start to node n
    h(n) = estimated cost from node n to goal
    """
    open_list = []
    heapq.heappush(open_list, (heuristic[start], start))

    g_cost = {start: 0}
    parent = {start: None}

    while open_list:
        f_current, current = heapq.heappop(open_list)

        # Check if the goal is reached
        if current == goal:
            path = []

            while current is not None:
                path.append(current)
                current = parent[current]

            path.reverse()
            return path, g_cost[goal]

        # Explore neighbouring nodes
        for neighbor, cost in graph[current]:
            new_g = g_cost[current] + cost

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f_neighbor = new_g + heuristic[neighbor]

                heapq.heappush(
                    open_list,
                    (f_neighbor, neighbor)
                )

                parent[neighbor] = current

    return None, float('inf')


# Main Program
if __name__ == "__main__":
    start_node = 'A'
    goal_node = 'E'

    print("Graph Adjacency List with Edge Weights:")
    for node, edges in graph.items():
        print(f"  {node} -> {edges}")

    print()
    print("Heuristic Table h(n):", heuristic)
    print()

    path, cost = a_star(graph, heuristic, start_node, goal_node)

    print(f"Executing A* Search from '{start_node}' to '{goal_node}':")
    print("Shortest Path:", " -> ".join(path) if path else "No path found")
    print("Total Cost:", cost)
