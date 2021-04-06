"""
Merge Sort

This module defines the Top-Down Merge Sort functions

FUNCTIONS:
    - merge_sort(arr) -> list
    - merge(arr_one, arr_two, arr_temp) -> list
"""

__docformat__ = 'reStructuredText'


def merge_sort(arr: list) -> list:
    """
    Performs a Top-Down Merge Sort on unsorted array and returns sorted array

    Time complexity: O(n*log(n))

    :param arr: Unsorted array
    :type arr: list
    :return: Returns sorted array
    :rtype: list
    """

    # Recursively loops through array, halving array until left with individual elements
    # Once array is broken down, starts merging elements, sorting with each merge
    if len(arr) > 1:
        # Halve array at midpoint
        mid_index = len(arr) // 2
        left_arr = arr[:mid_index]
        right_arr = arr[mid_index:]
        # Recursively divide newly-formed subarray
        merge_sort(left_arr)
        merge_sort(right_arr)
        # Once done dividing array and subarrays, merge two halves and sort
        merge(left_arr, right_arr, arr)
    return arr


def merge(arr_one: list, arr_two: list, arr_temp: list) -> None:
    """
    Merges two arrays into a third sorted array

    :param arr_one: First sorted array to be merged
    :type arr_one: list
    :param arr_two: Second sorted array to be merged
    :type arr_two: list
    :param arr_temp: Array to hold merged values
    :type arr_temp: list
    """

    # i: counter variable for first array
    # j: counter variable for second array
    # k: counter variable for merged array
    i = j = k = 0
    # Start at first element in both arrays
    # Compare elements from both arrays and add smallest element to merged array
    # After adding smallest element, step to next element in same array
    # Iterate until finished comparing all elements of either array
    while i < len(arr_one) and j < len(arr_two):
        if arr_one[i] < arr_two[j]:
            arr_temp[k] = arr_one[i]
            i += 1
        else:
            arr_temp[k] = arr_two[j]
            j += 1
        k += 1
    # Add any leftover elements from either array to merged array
    while i < len(arr_one):
        arr_temp[k] = arr_one[i]
        i += 1
        k += 1
    while j < len(arr_two):
        arr_temp[k] = arr_two[j]
        j += 1
        k += 1
