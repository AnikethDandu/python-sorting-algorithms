def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        j_index = -1
        min_num = arr[i]
        for j in range(i + 1, n):
            if arr[j] < min_num:
                min_num = arr[j]
                j_index = j
        if j_index > -1:
            arr[i], arr[j_index] = arr[j_index], arr[i]
    return arr


print(selection_sort([3, 1, 2]))
