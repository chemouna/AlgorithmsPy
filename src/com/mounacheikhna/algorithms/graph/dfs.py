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
    for n in graph[v] - visited:
        recursiveDfs(graph, n, visited)
    return visited


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))

g = {'A': {'B', 'C'},
     'B': {'A', 'D', 'E'},
     'C': {'A', 'F'},
     'D': {'B'},
     'E': {'B', 'F'},
     'F': {'C', 'E'}}

# print(dfs(g, 'A'))
# print(recursiveDfs(g, 'A'))

# print(dfs(g, 'C'))
# print(recursiveDfs(g, 'C'))

print(list(dfs_paths(g, 'A', 'F')))
