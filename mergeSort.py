def mergeArrays(arr, st, mid, end):
    N1 = mid - st + 1
    N2 = end - mid

    L1 = []
    L2 = []

    for i in range(N1):
        L1.append(arr[st + i])
    
    for i in range(N2):
        L2.append(arr[mid + 1 + i])
    
    i = 0
    j = 0
    k = st

    while (i < len(L1) and j < len(L2)):
        if L1[i] < L2[j]:
            arr[k] = L1[i]
            i += 1
        else:
            arr[k] = L2[j]
            j += 1
        k += 1
    
    while (i < len(L1)):
        arr[k] = L1[i]
        i += 1
        k += 1

    while (j < len(L2)):
        arr[k] = L2[j]
        j += 1
        k += 1

def mergeSort(arr, st, end):
    if (st < end):
        mid = int(st + (end - st) / 2)
        mergeSort(arr, st, mid)
        mergeSort(arr, mid + 1, end)

        mergeArrays(arr, st, mid, end)

L = [1,5,7,8,3,5,7,4,3,5,7,2]
mergeSort(L, 0, len(L) - 1)
print(L)