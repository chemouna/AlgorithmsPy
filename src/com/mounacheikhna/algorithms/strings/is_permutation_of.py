def is_permutation_of(str1, str2):
    if len(str1) != len(str2):
        return False
    hash_table = {}
    for c in str1:
        if c in hash_table:
            hash_table[c] += 1
        else:
            hash_table[c] = 1
    for c in str2:
        if c not in hash_table:
            return False
        hash_table[c] -= 1
    for k in hash_table:
        if hash_table[k] != 0:
            return False
    return True


print(is_permutation_of("abcdefg", "badfgce"))
print(is_permutation_of("abcdefg", "dgbcafk"))
