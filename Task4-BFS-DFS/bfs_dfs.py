"""
CCS 2226 - Foundations of Artificial Intelligence
Task Four - Search and Optimization

BFS (Breadth First Search) and DFS (Depth First Search)
Both programs output the search path from initial node to goal state.
"""

from collections import deque

# ─────────────────────────────────────────────
# GRAPH DEFINITION
# ─────────────────────────────────────────────

# A simple graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C', 'I'],
    'H': ['E'],
    'I': ['G']
}

# ─────────────────────────────────────────────
# BREADTH FIRST SEARCH (BFS)
# ─────────────────────────────────────────────

def bfs(graph, start, goal):
    """
    BFS explores nodes level by level using a queue (FIFO).
    It always finds the shortest path to the goal.

    Args:
        graph : adjacency list of the graph
        start : starting node
        goal  : target node

    Returns:
        path from start to goal, or None if not found
    """
    print("\n" + "="*50)
    print("BREADTH FIRST SEARCH (BFS)")
    print(f"Start: {start}  |  Goal: {goal}")
    print("="*50)

    # Queue holds the path taken so far
    queue = deque()
    queue.append([start])

    # Track visited nodes to avoid revisiting
    visited = set()
    visited.add(start)

    while queue:
        # Take the first path from the queue
        path = queue.popleft()
        current = path[-1]

        print(f"Visiting: {current}  |  Path so far: {' -> '.join(path)}")

        # Check if we reached the goal
        if current == goal:
            print(f"\nGoal '{goal}' found!")
            print(f"Final Path: {' -> '.join(path)}")
            print(f"Total nodes visited: {len(visited)}")
            return path

        # Add unvisited neighbors to the queue
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                queue.append(new_path)

    print(f"Goal '{goal}' not found.")
    return None


# ─────────────────────────────────────────────
# DEPTH FIRST SEARCH (DFS)
# ─────────────────────────────────────────────

def dfs(graph, start, goal):
    """
    DFS explores nodes by going as deep as possible using a stack (LIFO).
    It may not find the shortest path but uses less memory than BFS.

    Args:
        graph : adjacency list of the graph
        start : starting node
        goal  : target node

    Returns:
        path from start to goal, or None if not found
    """
    print("\n" + "="*50)
    print("DEPTH FIRST SEARCH (DFS)")
    print(f"Start: {start}  |  Goal: {goal}")
    print("="*50)

    # Stack holds the path taken so far
    stack = [[start]]

    # Track visited nodes to avoid revisiting
    visited = set()
    visited.add(start)

    while stack:
        # Take the last path from the stack
        path = stack.pop()
        current = path[-1]

        print(f"Visiting: {current}  |  Path so far: {' -> '.join(path)}")

        # Check if we reached the goal
        if current == goal:
            print(f"\nGoal '{goal}' found!")
            print(f"Final Path: {' -> '.join(path)}")
            print(f"Total nodes visited: {len(visited)}")
            return path

        # Add unvisited neighbors to the stack
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = path + [neighbor]
                stack.append(new_path)

    print(f"Goal '{goal}' not found.")
    return None


# ─────────────────────────────────────────────
# MAIN - RUN BOTH SEARCHES
# ─────────────────────────────────────────────

if __name__ == "__main__":

    print("\nGraph Structure:")
    for node, neighbors in graph.items():
        print(f"  {node} -> {neighbors}")

    start_node = 'A'
    goal_node  = 'I'

    # Run BFS
    bfs_path = bfs(graph, start_node, goal_node)

    # Run DFS
    dfs_path = dfs(graph, start_node, goal_node)

    # Summary comparison
    print("\n" + "="*50)
    print("SUMMARY")
    print("="*50)
    print(f"BFS Path: {' -> '.join(bfs_path) if bfs_path else 'Not found'}")
    print(f"DFS Path: {' -> '.join(dfs_path) if dfs_path else 'Not found'}")
    print("\nBFS finds the SHORTEST path.")
    print("DFS goes DEEP first and may find a longer path.")
