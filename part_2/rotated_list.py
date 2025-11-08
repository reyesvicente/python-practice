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


"""
    Let me explain the code line by line:

    python
    def rotate_list(lst, k):
        # Edge case: if list is None or no rotation needed
        if lst is None or k == 0:
            return lst  # Return the list as-is

        # Handle cases where k is larger than list length
        # Using modulo operation to get effective rotation count
        k = k % len(lst)  # Fixed: Changed '==' to '=' for assignment

        # If after modulo, k becomes 0, return list as-is
        if k == 0:
            return lst  # Fixed: Return 'lst' instead of 'list'

        # Create the rotated list by:
        # 1. Taking the last k elements (lst[-k:])
        # 2. Adding them to the beginning of the remaining elements (lst[:-k])
        rotated = lst[-k:] + lst[:-k]
        return rotated

    # Test cases
    print(rotate_list([1, 2, 3, 4, 5], 2))  # Should print [4, 5, 1, 2, 3]
    print(rotate_list([1, 2, 3, 4, 5], 1))  # Should print [5, 1, 2, 3, 4]
    Key Points:
    Edge Case Handling:
    Returns immediately if the list is None or no rotation is needed (k=0).
    Modulo Operation:
    k = k % len(lst) ensures k is within the list's bounds, handling cases where k is larger than the list length.
    List Slicing:
    lst[-k:] gets the last k elements.
    lst[:-k] gets all elements except the last k elements.
    Concatenating these gives the rotated list.
    Test Cases:
    The function is tested with two examples to ensure it works as expected.
    Example Walkthrough:
    For
    rotate_list([1, 2, 3, 4, 5], 2)
    :

    k = 2 % 5 = 2
    lst[-k:] is [4, 5]
    lst[:-k] is [1, 2, 3]
    Result: [4, 5] + [1, 2, 3] = [4, 5, 1, 2, 3]
"""