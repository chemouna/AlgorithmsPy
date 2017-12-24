def tarjanscc(g):
    """Returns the strongly connected components of a graph"""
    s = []
    s_set = set()
    index = {}
    lowlink = {}
    ret = []

    def dfs(v):
        index[v] = len(index)
        lowlink[v] = index[v]
        s.append(v)
        s_set.add(v)

        for w in g.get(v, ()):
            if w not in index:
                dfs(w)
                lowlink[v] = min(lowlink[v], lowlink[w])
            elif w in s_set:
                lowlink[v] = min(lowlink[v], index[w])

        if lowlink[v] == index[v]:
            scc = []
            w = None
            while v != w:
                w = s.pop()
                scc.append(w)
                s_set.remove(w)
            ret.append(scc)

    for v in g:
        if v not in index:
            dfs(v)

    return ret


g = {1: [2], 2: [1, 5], 3: [4], 4: [3, 5], 5: [6], 6: [7], 7: [8], 8: [6, 9], 9: []}
res = tarjanscc(g)

print "res: "
print res
