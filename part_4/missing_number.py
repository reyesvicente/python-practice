# ============================================================================
# PROBLEM 35: Missing Number in Range
# ============================================================================
# Write a function that finds the missing number in a list containing numbers from 1 to n.
# The list is unsorted and may have duplicates. Find any missing number.
# Example: missing_number([1, 2, 4, 5]) should return 3
# Example: missing_number([3, 1, 2, 4, 5, 6, 8]) should return 7

def missing_number(lst):
    """
    PSEUDOCODE:
    1. If the list is empty, return 1.
    2. Convert the list to a set `num_set` to remove duplicates and enable O(1) lookups.
    3. Find the maximum value in the list, let's call it `max_val`.
    4. Iterate through numbers `i` from 1 to `max_val`:
        a. If `i` is not in `num_set`:
            - Return `i` (found the missing number).
    5. If the loop finishes without returning:
        - Return `max_val + 1` (the sequence is complete up to max_val, so the next missing is max_val + 1).
    """
    if lst is None or len(lst) == 0:
        return 1
    num_set = set(lst)
    max_val = max(num_set)
    for i in range(1, max_val + 1):
        if i not in num_set:
            return i
    return max_val + 1

print(missing_number([1, 2, 4, 5]))
print(missing_number([3, 1, 2, 4, 5, 6, 8]))