def topological_sort(graph):
    topologicalSortedList = []
    zeroInDegreeVertexList = []

    inDegree = {u: 0 for u in graph}

    # step 1: iterate through the graph to get in-degree of each node
    for u in graph:
        for v in graph[u]:
            inDegree[v] += 1

    # step 2: iterate to get all nodes with in-degree 0
    for k in inDegree:
        if inDegree[k] == 0:
            zeroInDegreeVertexList.append(k)

    # step 3: process the nodes to get the topological sort
    while zeroInDegreeVertexList:
        v = zeroInDegreeVertexList.pop()
        topologicalSortedList.append(v)
        # go through all the nodes adjacent to v and update their in-degree since v is removed
        for u in graph[v]:
            inDegree[u] -= 1
            if inDegree[u] == 0:
                zeroInDegreeVertexList.append(u)

    return topologicalSortedList


def dfs_topological_sort(graph):
    L = []
    color = {u: "white" for u in graph}
    found_cycle = [False]
    for v in graph:
        if color[v] == "white":
            dfs_visit(graph, v, color, found_cycle, L)
        if found_cycle[0]:
            print("Graph has cycles!")
            break
    return L


def dfs_visit(graph, v, color, found_cycle, L):
    if found_cycle[0]:
        return
    color[v] = "gray"
    for w in graph[v]:
        if color[w] == "gray":
            found_cycle[0] = True
            return
        if color[w] == "white":
            dfs_visit(graph, w, color, found_cycle, L)
    color[v] = "black"
    L.append(v)


# Adjacency list
aGraph = {
    'A': set([]),
    'B': set(['A']),
    'C': set(['B'])
}
result = topological_sort(aGraph)
print("Topological sort >>> ", result)
if len(result) == len(aGraph):
    print("Directed Acyclic Graph!")
else:
    print("Graph has cycles!")

print("DFS Topological sort >>> ", result)
