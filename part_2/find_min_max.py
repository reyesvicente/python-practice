# ============================================================================
# PROBLEM 14: Find Largest and Smallest
# ============================================================================
# Write a function that returns both the largest and smallest numbers in a list.
# Return them as a tuple (min, max).
# Example: find_min_max([3, 1, 4, 1, 5, 9]) should return (1, 9)
# Do NOT use built-in min() or max() functions.

def find_min_max(lst):
    """
        FUNCTION find_min_max(lst):
        IF length of lst is 0:
            RETURN None  # or raise an error, depending on requirements

        # Initialize min and max with the first element
        min_val = lst[0]
        max_val = lst[0]

        # Iterate through the list starting from the second element
        FOR each number IN lst[1:]:
            IF number < min_val:
                min_val = number
            IF number > max_val:
                max_val = number

        RETURN (min_val, max_val)`
    """
    if len(lst) == 0:
        return None

    min_val = lst[0]
    max_val = lst[0]

    for num in lst:
        if num < min_val:
            min_val = num
        elif num > max_val:
            max_val = num
    return (min_val, max_val)


print(find_min_max([3, 1, 4, 1, 5, 9]))

"""
Here's a line-by-line explanation of the code:

python
def find_min_max(lst):
    """
    Function to find the minimum and maximum values in a list.
    Returns a tuple containing (minimum, maximum).
    """
    if len(lst) == 0:  # Check if the list is empty
        return None    # Return None if the list is empty

    # Initialize both min and max with the first element of the list
    min_val = lst[0]  # Start with the first element as the minimum
    max_val = lst[0]  # Start with the first element as the maximum

    # Iterate through each number in the list
    for num in lst:
        # Check if current number is smaller than current min
        if num < min_val:
            min_val = num  # Update min if current number is smaller
        # Check if current number is larger than current max
        elif num > max_val:
            max_val = num  # Update max if current number is larger

    # Return the found min and max as a tuple
    return (min_val, max_val)

# Example usage
print(find_min_max([3, 1, 4, 1, 5, 9]))  # Output will be (1, 9)
Key Points:

Handles empty lists by returning None
Initializes both min and max with the first element
Uses a single loop to find both min and max
Returns the result as a tuple (min, max)
The example call with [3, 1, 4, 1, 5, 9] correctly returns (1, 9)
"""