# ============================================================================
# PROBLEM 10: Flatten a Nested List
# ============================================================================
# Write a function that flattens a nested list into a single-level list.
# Example: flatten([[1, 2], [3, 4], [5, 6]]) should return [1, 2, 3, 4, 5, 6]
# Example: flatten([1, [2, 3], [[4, 5], 6]]) should return [1, 2, 3, 4, 5, 6]

def flatten(nested_list):
    """
        PSEUDO CODE:
        result = empty list

        for item in nested_list:
            if item is a list:
                flattened_sublist = flatten(item)  # Recursively flatten the sublist
                append all elements from flattened_sublist to result
            else:
                append item to result

        return result
    """
    result = []
    for item in nested_list:
        if isinstance(item, list):
            flattened_sublist = flatten(item)
            result.extend(flattened_sublist)
        else:
            result.append(item)
    return result

print(flatten([[1, 2], [3, 4], [5, 6]]))
print(flatten([1, [2, 3], [[4, 5], 6]]))


"""
    Let me break down the code line by line:

    python
    def flatten(nested_list):
    Defines a function called
    flatten
    that takes nested_list as input.
    python
        result = []
    Initializes an empty list called result to store the flattened elements.
    python
        for item in nested_list:
    Begins iterating through each element in the input nested_list.
    python
            if isinstance(item, list):
    Checks if the current item is a list using isinstance(). This handles nested lists.
    python
                flattened_sublist = flatten(item)
    If item is a list, recursively calls
    flatten()
    on it to handle any nested lists within it.
    python
                result.extend(flattened_sublist)
    Extends the result list with all elements from the flattened sublist, adding them as individual elements.
    python
            else:
                result.append(item)
    If item is not a list, directly appends it to result.
    python
        return result
    Returns the final flattened list after processing all elements.
    python
    print(flatten([[1, 2], [3, 4], [5, 6]]))  # Output: [1, 2, 3, 4, 5, 6]
    print(flatten([1, [2, 3], [[4, 5], 6]]))  # Output: [1, 2, 3, 4, 5, 6]
    Test cases that demonstrate the function working with different levels of nested lists.
    The function uses recursion to handle any level of nesting, making it flexible for various input structures.
"""