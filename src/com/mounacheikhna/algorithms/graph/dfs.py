def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


def recursiveDfs(graph, v, visited=None):
    if visited is None:
        visited = set()
    visited.add(v)
    for next in graph[v] - visited:
        recursiveDfs(graph, next, visited)
    return visited

g = {'A': {'B', 'C'},
     'B': {'A', 'D', 'E'},
     'C': {'A', 'F'},
     'D': {'B'},
     'E': {'B', 'F'},
     'F': {'C', 'E'}}
print(dfs(g, 'A'))
print(recursiveDfs(g, 'A'))

print(dfs(g, 'C'))
print(recursiveDfs(g, 'C'))

