def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        for j in range(i-1, -1, -1):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                i -= 1
            else:
                break
    return arr
