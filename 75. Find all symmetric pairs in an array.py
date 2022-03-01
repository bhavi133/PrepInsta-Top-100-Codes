Link : https://prepinsta.com/python-program/finding-symmetric-pairs-in-an-array/

def symmetric_pairs(arr):
    s = set()
    for (i, j) in arr:
        s.add((i, j))
        if (j, i) in s:
            print((i, j))

arr = [(3, 4), (1, 2), (5, 2), (7, 10), (4, 3), (2, 5)]
symmetric_pairs(arr)
