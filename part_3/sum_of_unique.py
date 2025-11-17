# ============================================================================
# PROBLEM 27: Sum of Unique Elements
# ============================================================================
# Write a function that returns the sum of all unique elements in a list.
# An element is unique if it appears exactly once.
# Example: sum_of_unique([1, 2, 2, 3, 3, 3]) should return 1
# Example: sum_of_unique([1, 1, 1, 1]) should return 0
# Example: sum_of_unique([5, 4, 3, 2, 1]) should return 15

def sum_of_unique(lst):
    """
        PSEUDO CODE:
        1. Create an empty dictionary to store the frequency of each element
        2. Iterate through the list and update the frequency of each element in the dictionary
        3. Initialize a variable to store the sum of unique elements
        4. Iterate through the dictionary and add the unique elements to the sum
        5. Return the sum of unique elements
    """
    """
    Calculate the sum of all unique elements in a list.
    An element is considered unique if it appears exactly once.

    Args:
        lst: List of integers

    Returns:
        int: Sum of unique elements in the list
    """
    # Initialize an empty dictionary to store the frequency of each number
    count = {}

    # Count the occurrences of each number in the list
    for num in lst:
        # If number is already in dictionary, increment its count
        if num in count:
            count[num] += 1
        else:
            # Otherwise, initialize its count to 1
            count[num] = 1

    # Initialize total sum to 0
    total = 0

    # Iterate through the dictionary items (number and its count)
    for num, cnt in count.items():
        # If the count is 1, add the number to total
        if cnt == 1:
            total += num

    # Return the total sum of unique elements
    return total

print(sum_of_unique([1, 2, 2, 3, 3, 3]))
print(sum_of_unique([1, 1, 1, 1]))
print(sum_of_unique([5, 4, 3, 2, 1]))