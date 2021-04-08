"""
Insertion Sort

This module defines the Insertion Sort function

FUNCTIONS:
    - insertion_sort(arr) -> list
"""

__docformat__ = 'reStructuredText'


def insertion_sort(arr: list) -> list:
    """
    Performs an Insertion Sort on unsorted array and returns sorted array

    Time complexity: O(n^2)

    :param arr: Unsorted array
    :type arr: list
    :return: Returns sorted array
    :rtype: list
    """

    # n: length of array
    # i: counter variable for iterating through array elements
    # j: counter variable for comparing element to previous element

    # Loop through array starting at index 1
    # Compare each element to previous element
    # If current element smaller, swap and repeat until comparison fails
    n = len(arr)
    for i in range(1, n):
        for j in range(i - 1, -1, -1):
            if arr[i] < arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                i -= 1
            else:
                break
    return arr
