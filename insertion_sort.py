def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        count = 0
        for j in range(i-1, -1, -1):
            if arr[i-count] < arr[j]:
                arr[i-count], arr[j] = arr[j], arr[i-count]
                count += 1
    return arr


print(insertion_sort([5, 4, 3, 2, 1, 0]))
