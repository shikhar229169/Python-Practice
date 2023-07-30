def lessthan(lst, k):
    arr = [i for i in lst if i < k]
    return arr

print(lessthan([1, -2, 0, 5, -3], 0))