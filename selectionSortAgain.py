def selectionSort(arr):
    N = len(arr)
    for i in range(N):
        maxIdx = 0
        for j in range(1, N - i):
            if (arr[j] > arr[maxIdx]):
                maxIdx = j
        arr[maxIdx], arr[N - i - 1] = arr[N - i - 1], arr[maxIdx]

def selectionSort_(arr):
    N = len(arr)
    for i in range(N - 1):
        minIdx = i
        for j in range(i, N):
            if (arr[j] < arr[minIdx]):
                minIdx = j
        arr[i], arr[minIdx] = arr[minIdx], arr[i]

arr = [2,4,1,4,6,7,3,1,3,5,23,12,56,32,1,2]
selectionSort_(arr)
print(arr)