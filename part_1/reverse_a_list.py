# ============================================================================
# PROBLEM 5: Reverse a List (without using reverse())
# ============================================================================
# Write a function that reverses a list without using the built-in reverse()
# or slicing with [::-1].
# Example: reverse_list([1, 2, 3, 4]) should return [4, 3, 2, 1]

def reverse_list(lst):
    """
        PSEUDO CODE:
        create an empty list called reversed_list
        for each element in lst starting from the last element to the first:
            append the element to reversed_list
    """
    reversed_list = []
    for i in range(len(lst)-1, -1, -1):
        reversed_list.append(lst[i])

    return reversed_list

print(reverse_list([1, 2, 3, 4]))

"""
    Let me break down the code line by line:

    python
    def reverse_list(lst):
    Defines a function named
    reverse_list
    that takes one parameter lst (a list).
    python
            PSEUDO CODE:
            create an empty list called reversed_list
            for each element in lst starting from the last element to the first:
                append the element to reversed_list
    This is a docstring that explains the function's purpose and includes pseudocode.
    python
        reversed_list = []
    Creates an empty list called reversed_list to store the reversed elements.
    python
        for i in range(len(lst)-1, -1, -1):
    Starts a loop that will iterate from the last index of the list to the first (0).
    len(lst)-1 is the starting index (last element)
    -1 is the stopping index (stops before -1, so 0 is included)
    -1 is the step (counts backwards)
    python
            reversed_list.append(lst[i])
    For each iteration, it takes the element at index i from the original list and appends it to reversed_list.
    python
        return reversed_list
    Returns the new list with elements in reverse order.
    python
    print(reverse_list([1, 2, 3, 4]))
    Calls the function with [1, 2, 3, 4] and prints the result [4, 3, 2, 1].
    Example with [1, 2, 3, 4]:

    1. i starts at 3 (last index), appends 4 to reversed_list
    2. i becomes 2, appends 3
    3. i becomes 1, appends 2
    4. i becomes 0, appends 1
    5. Returns [4, 3, 2, 1]
"""
