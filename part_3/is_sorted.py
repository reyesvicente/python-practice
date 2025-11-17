# ============================================================================
# PROBLEM 26: Is Sorted
# ============================================================================
# Write a function that checks if a list is sorted in ascending or descending order.
# Return True if sorted, False otherwise.
# Example: is_sorted([1, 2, 3, 4, 5]) should return True
# Example: is_sorted([5, 4, 3, 2, 1]) should return True
# Example: is_sorted([1, 3, 2, 4, 5]) should return False

def is_sorted(lst):
    """
        PSEUDO CODE:
        1. If list is empty or has 1 item: return True
        2. Check if all items are increasing (each item <= next item)
        3. If not, check if all items are decreasing (each item >= next item)
        4. Return True if either check passes, False otherwise
    """
    """
        Check if a list is sorted in either ascending or descending order.

        Args:
            lst: List of comparable items (numbers, strings, etc.)

        Returns:
            bool: True if the list is sorted in ascending or descending order, False otherwise
    """
    # Handle edge cases: empty list or single element list is always sorted
    if len(lst) <= 1:
        return True

    # Check if the list might be in ascending order (first two elements suggest this)
    if lst[0] <= lst[1]:
        # Verify all subsequent elements are in non-decreasing order
        for i in range(1, len(lst)):
            if lst[i] < lst[i - 1]:  # If any element is smaller than the previous
                return False
        return True  # All elements are in non-decreasing order
    else:
        # If not ascending, check for descending order
        for i in range(1, len(lst)):
            if lst[i] > lst[i - 1]:  # If any element is larger than the previous
                return False
        return True  # All elements are in non-increasing order

# Test cases
print(is_sorted([1, 2, 3, 4, 5]))  # True (ascending)
print(is_sorted([5, 4, 3, 2, 1]))  # True (descending)
print(is_sorted([1, 3, 2, 4, 5]))  # False (not sorted)

"""

"""