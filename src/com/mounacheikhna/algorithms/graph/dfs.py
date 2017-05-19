def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited


def recursive_dfs(graph, v, visited=None):
    if visited is None:
        visited = set()
    visited.add(v)
    for n in graph[v] - visited:
        recursive_dfs(graph, n, visited)
    return visited


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for n in graph[vertex] - set(path):
            if n == goal:
                yield path + [n]
            else:
                stack.append((n, path + [n]))


def recursive_dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for n in graph[start] - set(path):
        yield from recursive_dfs_paths(graph, n, goal, path + [n])

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
print(list(recursive_dfs_paths(g, 'A', 'F')))
