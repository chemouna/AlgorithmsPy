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

# Adjacency list
graph = {
    'A': set([]),
    'B': set(['A']),
    'C': set(['B'])
}
result = topological_sort(graph)
print("Topological sort >>> ", result)
# check if #nodes in result == #nodes in graph
if len(result) == len(graph):
    print("Directed Acyclic Graph!")
else:
    print("Graph has cycles!")
