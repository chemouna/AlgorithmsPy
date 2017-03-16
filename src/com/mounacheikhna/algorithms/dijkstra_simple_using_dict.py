import collections
import math

class Graph:
    '''
    '''

    def __init__(self):
        self.vertices = set()

        # makes the default value for all vertices an empty list
        self.edges = collections.defaultdict(list)
        self.weights = {}

    def add_vertex(self, value):
        self.vertices.add(value)

    def add_edge(self, from_vertex, to_vertex, distance):
        if from_vertex == to_vertex: pass  # no cycles allowed
        self.edges[from_vertex].append(to_vertex)
        self.weights[(from_vertex, to_vertex)] = distance

    def __str__(self):
        string = "Vertices: " + str(self.vertices) + "\n"
        string += "Edges: " + str(self.edges) + "\n"
        string += "Weights: " + str(self.weights)
        return string


def dijkstra(graph, start):
    # initializations
    S = set()

    # dist represents the length shortest distance paths from start -> v, for v in dist.
    # We initialize it so that every vertex has a path of infinity
    dist = dict.fromkeys(list(graph.vertices), math.inf)
    pred = dict.fromkeys(list(graph.vertices), None)

    # then we set the path length of the start vertex to 0
    dist[start] = 0

    # while there exists a vertex v not in S
    while S != graph.vertices:
        # let v be the closest vertex that has not been visited...it will begin at 'start'
        v = min((set(dist.keys()) - S), key=dist.get)

        # for each neighbor of v not in S
        for neighbor in set(graph.edges[v]) - S:
            new_path = dist[v] + graph.weights[v, neighbor]

            # is the new path from neighbor through
            if new_path < dist[neighbor]:
                # since it's optimal, update the shortest path for neighbor
                dist[neighbor] = new_path

                # set the pred vertex of neighbor to v
                pred[neighbor] = v
        S.add(v)

    return dist, pred


def shortest_path(graph, start, end):
    '''Uses dijkstra function in order to output the shortest path from start to end
    '''

    dist, previous = dijkstra(graph, start)

    path = []
    vertex = end

    while vertex is not None:
        path.append(vertex)
        vertex = previous[vertex]

    path.reverse()
    return path


# To run an example
G = Graph()
G.add_vertex('a')
G.add_vertex('b')
G.add_vertex('c')
G.add_vertex('d')
G.add_vertex('e')

G.add_edge('a', 'b', 2)
G.add_edge('a', 'c', 8)
G.add_edge('a', 'd', 5)
G.add_edge('b', 'c', 1)
G.add_edge('c', 'e', 3)
G.add_edge('d', 'e', 4)

print(G)

print(dijkstra(G, 'a'))
print("Shortest Path: ")
print(shortest_path(G, 'a', 'e'))
