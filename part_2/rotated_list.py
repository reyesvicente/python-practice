# ============================================================================
# PROBLEM 17: Rotate List
# ============================================================================
# Write a function that rotates a list by k positions to the right.
# Example: rotate_list([1, 2, 3, 4, 5], 2) should return [4, 5, 1, 2, 3]
# Example: rotate_list([1, 2, 3, 4, 5], 1) should return [5, 1, 2, 3, 4]

def rotate_list(lst, k):
    """
        PSEUDO CODE
        function rotate_list(lst, k):
        # Handle edge cases
        if list is empty or k is 0:
            return list

        # Handle case where k is larger than list length
        k = k % length of list

        # No rotation needed
        if k == 0:
            return list

        # Split the list into two parts
        # First part: elements from (length - k) to end
        # Second part: elements from start to (length - k - 1)
        rotated = lst[-k:] + lst[:-k]

        return rotated
    """
    if lst is None or k == 0:
        return lst

    k == k % len(lst)

    if k == 0:
        return list

    rotated = lst[-k:] + lst[:-k]
    return rotated

print(rotate_list([1, 2, 3, 4, 5], 2))
print(rotate_list([1, 2, 3, 4, 5], 1))