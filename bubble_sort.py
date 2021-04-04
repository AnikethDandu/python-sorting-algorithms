def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


print(bubble_sort([7, 2, 4, 5, 9, 1, 4, 0, 2, 34, 5]))
