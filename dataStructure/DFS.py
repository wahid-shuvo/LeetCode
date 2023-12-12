def depth_first_search(graph, start, visited):
    visited[start] = True
    print(start,end=' ')

    for adjacent_node in graph[start]:
        if not visited[adjacent_node]:
            depth_first_search(graph,adjacent_node,visited)

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
visited_nodes={node: False for node in graph}
depth_first_search(graph,'A',visited_nodes)