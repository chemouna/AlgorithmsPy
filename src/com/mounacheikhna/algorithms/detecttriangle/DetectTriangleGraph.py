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
        if root == node:
            return 1
        else:
            return 0
    else:
        res = 0
        for item in connections[node]:
            res += _dfs(level + 1, root, item, connections)
        return res


def get_num_triangles_dfs(list_node_pair):
    """
    @param list_node_pair, a list of edges which are
    represented as tuples.
    """
    nodes = set()
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
    mysum = 0
    for item in nodes:
        mysum += _dfs(0, item, item, connections)
    res = mysum / 6
    return res
