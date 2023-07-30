def selectionSort(arr):
    if (len(arr) == 0):
        return
    
    for i in range(len(arr)):
        currMinIdx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[currMinIdx]:
                currMinIdx = j
        arr[i], arr[currMinIdx] = arr[currMinIdx], arr[i]


arr = [5,3,2,6,7,3,2]
selectionSort(arr)
print(arr)