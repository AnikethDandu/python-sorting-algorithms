"""
Bubble Sort

This module defines the bubble sort method

FUNCTIONS:
    - bubble_sort(arr) -> list
"""

__docformat__ = 'reStructuredText'


def bubble_sort(arr: list) -> list:
    """
    Returns a sorted array using bubble sort

    Time complexity: O(n^2)

    :param arr: Array to be sorted
    :type arr: list
    :return: Sorted array
    :rtype: list
    """
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
