def depth_first_search(graph, start,visited):
    visited[start]=True
    print(start)

    for neighbour in graph[start]:
        if not visited[neighbour]:
            depth_first_search(graph,neighbour,visited)


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

visited={node: False for node in graph}
depth_first_search(graph,'A',visited)
