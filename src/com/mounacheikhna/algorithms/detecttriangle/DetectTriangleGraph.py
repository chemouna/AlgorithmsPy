"""
Given a undirected graph with corresponding edges. Find the number of
possible triangles?
Example:
0 1
2 1
0 2
4 1
Answer:
1
"""


def _dfs(level, root, node, connections):
    N = 3
    if level == N:
        return 1 if root == node else 0
    else:
        res = 0
        for item in connections[node]:
            res += _dfs(level + 1, root, item, connections)
        return res


def compute_connections(list_node_pair, nodes):
    connections = {}
    for item in list_node_pair:
        a = item[0]
        b = item[1]
        nodes.add(a)
        nodes.add(b)
        if a in connections:
            connections[a].append(b)
        else:
            connections[a] = [b]
        if b in connections:
            connections[b].append(a)
        else:
            connections[b] = [a]
    return connections


def get_num_triangles_dfs(list_node_pair):
    """
    @param list_node_pair, a list of edges which are
    represented as tuples.

    The algorithm used:

    """
    nodes = set()
    connections = compute_connections(list_node_pair, nodes)
    mysum = 0
    for item in nodes:
        mysum += _dfs(0, item, item, connections)
    return mysum / 6
