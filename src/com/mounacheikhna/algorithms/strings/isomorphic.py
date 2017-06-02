from collections import defaultdict


def IsIsoMorphic(a, b):
    dictA = dictB = defaultdict(str)
    for i, c in enumerate(a):
        dictA[c] = i
        dictB[b[i]] = i
    return encode(b, dictB) == encode(a, dictA)


def encode(a, dic):
    return ''.join(str(dic[c]) for c in a)
