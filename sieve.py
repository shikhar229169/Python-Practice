import math

def findPrimes(n):
    L = []
    for i in range(1, n+2):
        L.append(1)
    L[1] = 0

    for i in range(2, int(math.sqrt(n))+1):
        if (L[i]):
            for j in range(i*i, n+1, i):
                L[j] = 0

    for i in range(1, n+1):
        if (L[i]):
            print(i)

findPrimes(100)