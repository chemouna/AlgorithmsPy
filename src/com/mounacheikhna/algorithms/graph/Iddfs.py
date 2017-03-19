from collections import defaultdict


# This class represents a directed graph using adjacency
# list representation
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    # perform a Depth-Limited search from given source 'src'
    def dls(self, src, target, maxDepth):
        if src == target:
            return True

        # If reached the maximum depth, stop recursing.
        if maxDepth <= 0:
            return False

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[src]:
            if self.dls(i, target, maxDepth - 1):
                return True

        return False

    # IDDFS to search if target is reachable from v using dls
    def iddfs(self, src, target, maxDepth):
        # Repeatedly depth-limit search till the maximum depth
        for i in range(maxDepth):
            if self.dls(src, target, i):
                return True
        return False


g = Graph(7)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)

target = 6
maxDepth = 3
src = 0

if g.iddfs(src, target, maxDepth):
    print("Target is reachable from source " +
          "within max depth")
else:
    print("Target is NOT reachable from source " +
          "within max depth")
