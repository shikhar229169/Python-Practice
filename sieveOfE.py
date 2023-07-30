from math import sqrt

N = int(input("Enter Number: "))

isPrime = []
for i in range(0, N + 1):
    isPrime.append(1)

isPrime[0] = 0
isPrime[1] = 0

for i in range(2, int(sqrt(N)) + 1):
    if (isPrime[i]):
        for j in range(i * i, N + 1, i):
            isPrime[j] = 0

for i in range(N + 1):
    if (isPrime[i]):
        print(i)