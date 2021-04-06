def merge_sort(arr):
    if len(arr) > 1:
        mid_index = len(arr) // 2
        left_arr = arr[:mid_index]
        right_arr = arr[mid_index:]
        merge_sort(left_arr)
        merge_sort(right_arr)


merge_sort([0, 1, 2, 3, 4, 5])