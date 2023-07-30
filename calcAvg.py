def average(arr):
    try:
        totalSum = sum(arr)
        return totalSum / len(arr)
    except ZeroDivisionError:
        return 0.0


print((lambda x, y: y - 2 * x) (1, 11))
print(average([]))