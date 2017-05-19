def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

g = {'A': {'B', 'C'},
     'B': {'A', 'D', 'E'},
     'C': {'A', 'F'},
     'D': {'B'},
     'E': {'B', 'F'},
     'F': {'C', 'E'}}

print(bfs(g, 'A'))

