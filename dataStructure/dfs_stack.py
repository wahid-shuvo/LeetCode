def depth_first_search(graph, start):
    visited = {node: False for node in graph}

    stack = [start]

    while stack:
        current_node = stack.pop()
        if not visited[current_node]:
            print(current_node)
            visited[current_node] = True
        for next in graph[current_node]:
            if not visited[next]:
                stack.append(next)


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

print("Depth-First Traversal:")
depth_first_search(graph, 'A')
