def merge_sort(arr):
    if len(arr) > 1:
        mid_index = len(arr) // 2
        left_arr = arr[:mid_index]
        right_arr = arr[mid_index:]
        merge_sort(left_arr)
        merge_sort(right_arr)


def merge(arr_one, arr_two):
    arr_temp = [0] * (len(arr_one) + len(arr_two))
    i = j = k = 0
    while i < len(arr_one) and j < len(arr_two):
        if arr_one[i] < arr_two[j]:
            arr_temp[k] = arr_one[i]
            i += 1
        else:
            arr_temp[k] = arr_two[j]
            j += 1
        k += 1
    if i < len(arr_one):
        for x in range(i, len(arr_one)):
            arr_temp[i+x] = arr_one[x]
    if j < len(arr_two):
        for x in range(j, len(arr_two)):
            arr_temp[i+x] = arr_two[x]
    return arr_temp


print(merge([1, 2, 3, 5], [4, 7, 9]))
