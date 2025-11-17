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
    if len(lst) <= 1:
        return True
    if lst[0] <= lst[1]:
        for i in range(1, len(lst)):
            if lst[i] < lst[i - 1]:
                return False
        return True
    else:
        for i in range(1, len(lst)):
            if lst[i] > lst[i - 1]:
                return False
        return True


print(is_sorted([1, 2, 3, 4, 5]))
print(is_sorted([5, 4, 3, 2, 1]))
print(is_sorted([1, 3, 2, 4, 5]))
