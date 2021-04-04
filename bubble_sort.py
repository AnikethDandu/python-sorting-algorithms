def bubble_sort(array):
    for i in range(len(array)):
        if i < len(array)-1:
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]


bubble_sort([1, 2, 3, 0])
