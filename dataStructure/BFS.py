def breadth_first_search(graph, start):
    visited={node:False for node in graph}
    queue=[start]
    visited[start]=True

    while queue:
        current_node=queue.pop(0)
        print(current_node)
        for next in graph[current_node]:
            if not visited[next]:
                queue.append(next)
                visited[next]=True





graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B', 'E'],
    'E': ['B', 'D'],
    'F': ['C', 'H'],
    'G': ['C'],
    'H': ['F']
}

# Perform Breadth-First Traversal starting from node 'A'
print("Breadth-First Traversal:")
breadth_first_search(graph, 'A')
