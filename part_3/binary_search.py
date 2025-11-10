# ============================================================================
# PROBLEM 22: Binary Search
# ============================================================================
# Write a function that performs binary search on a sorted list.
# Return the index of the target if found, otherwise return -1.
# Assume the list is already sorted.
# Example: binary_search([1, 3, 5, 7, 9, 11], 7) should return 3
# Example: binary_search([1, 3, 5, 7, 9, 11], 6) should return -1
from math import floor

def binary_search(lst, target):
    """
        PSEUDO CODE
        1. Initialize two pointers, left and right, to the start and end of the list, respectively.
        2. While left is less than or equal to right:
            a. Calculate the middle index.
            b. If the middle element is the target, return its index.
            c. If the middle element is greater than the target, move the right pointer left.
            d. If the middle element is less than the target, move the left pointer right.
        3. If the target is not found, return -1.
    """
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = floor((left + right) / 2)
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(binary_search([1, 3, 5, 7, 9, 11], 7))
print(binary_search([1, 3, 5, 7, 9, 11], 6))