# ============================================================================
# PROBLEM 6: Duplicate Removal
# ============================================================================
# Write a function that removes duplicates from a list while maintaining order.
# Example: remove_duplicates([1, 2, 2, 3, 1, 4]) should return [1, 2, 3, 4]

def remove_duplicates(lst):
    """
        PSEUDO CODE:
        create an empty set called 'seen'
        create an empty list called 'result'

        for each item in lst:
            if item is not in seen:
                add item to seen
                append item to result
        return result
    """
    seen = set()
    result = []

    for i in lst:
        if i not in seen:
            seen.add(i)
            result.append(i)
    return result


print(remove_duplicates([1, 2, 2, 3, 1, 4]))

"""
    Let me break down the code line by line:

    python
    def remove_duplicates(lst):
    Defines a function named
    remove_duplicates
    that takes one parameter lst (a list).
    python
        PSEUDO CODE:
        create an empty set called 'seen'
        create an empty list called 'result'
        for each item in lst:
            if item is not in seen:
                add item to seen
                append item to result
        return result
    This is a docstring that explains the function's purpose and includes pseudocode.
    python
        seen = set()
    Creates an empty set called seen to keep track of unique elements we've encountered.
    python
        result = []
    Creates an empty list called result to store the final list without duplicates.
    python
        for i in lst:
    Starts a loop that iterates through each element in the input list lst.
    python
            if i not in seen:
    Checks if the current element i is not in the seen set (i.e., it's the first time we're seeing this element).
    python
                seen.add(i)
    If the element is not in seen, adds it to the set to mark it as seen.
    python
                result.append(i)
    Appends the element to the result list to maintain the order of first occurrence.
    python
        return result
    Returns the final list with duplicates removed, in the order of their first appearance.
    python
    print(remove_duplicates([1, 2, 2, 3, 1, 4]))
    Calls the function with [1, 2, 2, 3, 1, 4] and prints the result [1, 2, 3, 4].
    Example with [1, 2, 2, 3, 1, 4]:

    i = 1: Not in seen → add to seen and result
    seen: {1}
    result: [1]
    i = 2: Not in seen → add to seen and result
    seen: {1, 2}
    result: [1, 2]
    i = 2: Already in seen → skip
    i = 3: Not in seen → add to seen and result
    seen: {1, 2, 3}
    result: [1, 2, 3]
    i = 1: Already in seen → skip
    i = 4: Not in seen → add to seen and result
    seen: {1, 2, 3, 4}
    result: [1, 2, 3, 4]
    Final result: [1, 2, 3, 4]
"""