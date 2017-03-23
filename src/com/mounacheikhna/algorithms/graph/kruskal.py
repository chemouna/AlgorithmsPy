class WeightedGraph:
    edges = []
    weight = []
    vertices = []

    def __init__(self, edge_list, weight):
        self.edges.append(edge_list)
        self.weight.append(weight)

    def add(self, edge_list, weight):
        self.edges.append(edge_list)
        self.weight.append(weight)

    def makeset(self):
        for i in range(len(self.edges)):
            for j in range(len(self.edges[i])):
                if self.edges[i][j] not in self.vertices:  # i think its weird that somehow we have use cases where
                    # edge isn't already in vertices
                    self.vertices.append(self.edges[i][j])

        for k in range(len(self.vertices)):
            self.vertices[k] = [self.vertices[k]]  # why are the sets overriding the vertices ? -> this makes the first
            # element of the vertices array the head of the set

    def findset(self, vertex):
        for i in range(len(self.vertices)):
            for element in self.vertices[i]:
                if element == vertex:
                    return i

    def sortEdgesByWeight(self):
        if len(self.edges) != len(self.weight):
            return
        for i in range(1, len(self.weight)):
            temp_edge = self.edges[i]
            temp_weight = self.weight[i]
            current = i - 1
            while current >= 0 and temp_weight < self.weight[i]:
                self.weight[current + 1] = self.weight[current]
                self.edges[current + 1] = self.edges[current]
                current -= 1
            self.weight[current + 1] = temp_weight  # be careful here not to forget the additional +1
            self.edges[current + 1] = temp_edge

    def kruskal(self):
        self.sortEdgesByWeight()
        self.makeset()
        count = 0
        i = 0
        while len(self.vertices) > 1:
            if self.findset(self.edges[i][0]) != self.findset(self.edges[i][1]):
                count += 1
                self.union(self.edges[i][0], self.edges[i][1])
            i += 1

    def print_graph(self):
        """
        Print each set of edges in a graph and its corresponding edges
        """
        print(self.edges)
        print(self.weight)
        print(self.vertices)

    def union(self, vertex1, vertex2):
        index1 = self.findset(vertex1)
        index2 = self.findset(vertex2)
        for element in self.vertices[index2]:
            self.vertices[index1].append(element)
        self.vertices.pop(index2)


if __name__ == "__main__":
    test_graph = WeightedGraph([1, 2], 4)
    test_graph.add([1, 3], 2)
    test_graph.add([1, 5], 3)
    test_graph.add([2, 4], 5)
    test_graph.add([3, 4], 1)
    test_graph.add([3, 5], 6)
    test_graph.add([3, 6], 3)
    test_graph.add([4, 6], 6)
    test_graph.add([5, 6], 2)
    test_graph.kruskal()
    test_graph.print_graph()
