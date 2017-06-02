from collections import defaultdict


def IsIsoMorphic(a, b):
    dictA = dictB = defaultdict(str)
    for i, c in enumerate(a):
        dictA[c] = i
        dictB[b[i]] = i
    return encode(b, dictB) == encode(a, dictA)


def encode(a, dic):
    return ''.join(str(dic[c]) for c in a)


MAX_CHARS = 256


def areIsomorphic(str1, str2):
    m = len(str1)
    n = len(str2)

    # Length of both strings must be same for one to one
    # correspondance
    if m != n:
        return False

    # To mark visited characters in str2
    marked = [False] * MAX_CHARS

    # To store mapping of every character from str1 to
    # that of str2. Initialize all entries of map as -1
    map = [-1] * MAX_CHARS

    # Process all characters one by one
    for i in range(n):

        # if current character of str1 is seen first
        # time in it.
        if map[ord(str1[i])] == -1:

            # if current character of st2 is already
            # seen, one to one mapping not possible
            if marked[ord(str2[i])]:
                return False

            # Mark current character of str2 as visited
            marked[ord(str2[i])] = True

            # Store mapping of current characters
            map[ord(str1[i])] = str2[i]

        # If this is not first appearance of current
        # character in str1, then check if previous
        # appearance mapped to same character of str2
        elif map[ord(str1[i])] != str2[i]:
            return False

    return True
