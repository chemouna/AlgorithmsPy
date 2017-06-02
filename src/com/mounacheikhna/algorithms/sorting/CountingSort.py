
def countingsort(list, k):
    counter = [0] * (k + 1)
    for i in list:
        counter[i] += 1

    index = 0
    for i in range(len(counter)):
        while counter[i] > 0:
            list[index] = i

