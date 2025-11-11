# ============================================================================
# PROBLEM 24: Two Sum
# ============================================================================
# Write a function that finds two numbers in a list that add up to a target sum.
# Return the indices of the two numbers. Assume exactly one solution exists.
# Example: two_sum([2, 7, 11, 15], 9) should return (0, 1)
# Example: two_sum([3, 2, 4], 6) should return (1, 2)

def two_sum(lst, target):
    """
        FUNCTION two_sum(lst, target):
        // Create a dictionary to store value-index pairs
        value_to_index = {}

        // Iterate through the list with index and value
        FOR index, num IN enumerate(lst):
            // Calculate the complement needed to reach target
            complement = target - num

            // If complement exists in dictionary, we found our pair
            IF complement IN value_to_index:
                RETURN (value_to_index[complement], index)

            // Otherwise, add current number and its index to dictionary
            value_to_index[num] = index

        // This line should never be reached as per problem statement
        RETURN (-1, -1)
    """
    value_to_index = {}
    for i, num in enumerate(lst):
        complement = target - num

        if complement in value_to_index:
            return (value_to_index[complement], i)

        value_to_index[num] = i
    return (-1, -1)

print(two_sum([2, 7, 11, 15], 9))
print(two_sum([3, 2, 4], 6))
