from math import sqrt

def SOE(limit):
    st = 2
    end = limit

    isPrime = []
    primeNums = []

    for i in range(end + 1):
        isPrime.append(True)
    
    isPrime[0] = False
    isPrime[1] = False

    for i in range(2, int(sqrt(end)) + 1):
        if isPrime[i]:
            for j in range(i * i, end + 1, i):
                isPrime[j] = False

    for i in range (end + 1):
        if isPrime[i]:
            primeNums.append(i)

    print (primeNums)

SOE(100)
