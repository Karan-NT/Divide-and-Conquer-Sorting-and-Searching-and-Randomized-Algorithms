def mergeSort(arr):
    n = len(arr)
    tempArr = [0]*n
    return mergeSortAux(arr, tempArr, 0, n-1)

def mergeSortAux(arr, tempArr, left, right):
    invCount = 0

    if left < right:
        mid = (left + right)//2
        invCount += mergeSortAux(arr, tempArr, left, mid)
        invCount += mergeSortAux(arr, tempArr, mid + 1, right)
        invCount += merge(arr, tempArr, left, mid, right)

    return invCount

def merge(arr, tempArr, left, mid, right):
    i = left
    k = left
    j = mid + 1
    invCount = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            tempArr[k] = arr[i]
            i += 1
        else:
            tempArr[k] = arr[j]
            invCount += (mid-i + 1)
            j += 1

        k += 1

    while i <= mid:
        tempArr[k] = arr[i]
        k += 1
        i += 1

    while j <= right:
        tempArr[k] = arr[j]
        k += 1
        j += 1

    for q in range(left, right + 1):
        arr[q] = tempArr[q]

    return invCount

arr = [2, 12, 5, 1, 3, 8, 7, 15, 13]
print(mergeSort(arr))
