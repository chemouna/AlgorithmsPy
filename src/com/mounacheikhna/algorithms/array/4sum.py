
def fourSum(arr):
    sums = {}
    for a in arr:
        for b in arr:
            sums[a + b] = (a, b)

    for c in arr:
        for d in arr:
            if -(c + d) in sums:
                print (sums[-(c + d)][0], sums[-(c + d)][1], c, d)
                return

    print "No Solution"


a1 = [2, 3, 1, 0, -4, -1]
fourSum(a1)
