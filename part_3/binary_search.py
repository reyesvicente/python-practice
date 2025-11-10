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

"""
    Let me explain the code line by line:

    from math import floor - Imports the floor function from the math module to round down numbers.
    def binary_search(lst, target): - Defines the function that takes a sorted list and a target value.
    left = 0 - Initializes the left pointer to the start of the list (index 0).
    right = len(lst) - 1 - Initializes the right pointer to the last index of the list.
    while left <= right: - The main loop that continues as long as the left pointer hasn't passed the right pointer.
    mid = floor((left + right) / 2) - Calculates the middle index by averaging left and right, then rounding down.
    if lst[mid] == target: - Checks if the middle element is equal to the target.
    If true, returns the middle index.
    elif lst[mid] < target: - If the middle element is less than the target:
    left = mid + 1 - Moves the left pointer to the right of mid, eliminating the left half.
    else: - If the middle element is greater than the target:
    right = mid - 1 - Moves the right pointer to the left of mid, eliminating the right half.
    return -1 - Returns -1 if the loop completes without finding the target.
    print(binary_search([1, 3, 5, 7, 9, 11], 7)) - Test case that returns 3 (index of 7).
    print(binary_search([1, 3, 5, 7, 9, 11], 6)) - Test case that returns -1 (6 not in the list).
"""