def depth_first_search(graph, start):
    visited = {node: False for node in graph}
    stack = [start]

    while stack:
        current_node = stack.pop()

        if not visited[current_node]:
            print(current_node, end=' ')
            visited[current_node] = True

        for next_node in graph[current_node]:
            if not visited[next_node]:
                stack.append(next_node)


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
