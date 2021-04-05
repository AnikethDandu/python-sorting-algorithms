"""
Selection Sort

This module defines the selection sort method

FUNCTIONS:
    - selection_sort(arr) -> list
"""

__docformat__ = 'reStructuredText'


def selection_sort(arr: list) -> list:
    """
    Returns a sorted array using selection sort

    Time complexity: O(n^2)

    :param arr: Array to be sorted
    :type arr: list
    :return: Sorted array
    :rtype: list
    """
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index > i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
        print(arr)
    return arr
