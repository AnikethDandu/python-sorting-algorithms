"""
Selection Sort

This module defines the Selection Sort function

FUNCTIONS:
    - selection_sort(arr) -> list
"""

__docformat__ = 'reStructuredText'


def selection_sort(arr: list) -> list:
    """
    Performs a Selection Sort on unsorted array and returns sorted array

    Time complexity: O(n^2)

    :param arr: Unsorted array
    :type arr: list
    :return: Sorted array
    :rtype: list
    """

    # n: length of array
    # i: counter variable for iteration over array elements in range (0, n-1)
    # j: counter variable for comparing (i)th element to elements in range (i+1, n)
    # min_index: index for smallest element in range (i+1, n)

    # For array of n items, iterate from first to (n-1)th element
    # For each element, compare to every other element in array in range (i+1, n)
    # If smaller element exists beyond (i)th element, swap current and (j)th element
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index > i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
