from copy import *


class Scc:
    def __init__(self, g):
        super().__init__()
        self.visited = [False] * g.number_vertices
        self.stack = []
        self.g = g

    def kosaraju(self):
        """
        Determines SCC for a directed graph using Kosaraju's algorithm
        """

        # First pass to calculate finish time
        for i in range(self.g.number_vertices):
            if not self.visited[i]:
                self.visited[i] = True
                self.dfs(i)

        gg = copy(self.g)
        gg.transpose()

        # reset visited for the reversed graph
        self.visited = [False] * gg.number_vertices
        # connected components
        cc = []

        while len(self.stack) > 0:
            e = self.stack.pop()
            if not self.visited[e]:
                self.visited[e] = True
                cc.append(self.dfsT(e, gg))

        return cc

    def dfs(self, current):
        for v in self.g.neighbours(current):
            if not self.visited[v]:
                self.visited[v] = True
                self.dfs(v)
        self.stack.append(current)

    def dfsT(self, current, gg):
        sr = [current]
        for v in gg.neighbours(current):
            if not self.visited[v]:
                self.visited[v] = True
                sr += self.dfsT(current, gg)

        return sr


class DirectedGraph:
    def __init__(self, n):
        self.number_vertices = n
        self.adj = [[False for _ in range(n)] for _ in range(n)]

    def connect(self, u, v):
        self.adj[u][v] = True

    def disconnect(self, u, v):
        self.adj[u][v] = False

    def neighbours(self, u):
        return [v for v, con in enumerate(self.adj[u]) if con]

    def is_edge(self, u, v):
        return self.adj[u][v]

    def transpose(self):
        self.adj = [list(x) for x in zip(*self.adj)]


# Tests

Z = DirectedGraph(3)
Z.connect(0, 1)
Z.connect(1, 2)
Z.connect(2, 1)
print(Scc(Z).kosaraju()) # should

A = DirectedGraph(5)
A.connect(0, 1)
A.connect(1, 2)
A.connect(2, 0)

A.connect(1, 3)
A.connect(3, 4)
A.connect(4, 3)

print(Scc(A).kosaraju())

B = DirectedGraph(8)
B.connect(0, 1)
B.connect(1, 2)
B.connect(2, 1)

B.connect(3, 4)
B.connect(5, 3)
B.connect(4, 5)

B.connect(6, 7)

print(Scc(B).kosaraju())
