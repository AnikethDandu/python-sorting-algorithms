"""
Bubble Sort

This module defines the Bubble Sort function

FUNCTIONS:
    - bubble_sort(arr) -> list
"""

__docformat__ = 'reStructuredText'


def bubble_sort(arr: list) -> list:
    """
    Performs a Bubble Sort on unsorted array and returns sorted array

    Time complexity: O(n^2)

    :param arr: Unsorted array
    :type arr: list
    :return: Sorted array
    :rtype: list
    """

    # n: length of array
    # i: counter variable for iteration over array elements in range (0, n-1)
    # j: counter variable to compare each element with right adjacent element

    # For array of n items, iterate from first to (n-1)th element
    # For each iteration, compare every element to adjacent element in range (0, n-i-1) and swap if in wrong order
    # First iteration (i=0) places largest element at index n-1, second iteration (i=1) at n-2 so each successive
    # iteration can ignore last elements in array
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
