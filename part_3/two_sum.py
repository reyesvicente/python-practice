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


"""
    Let me break down the two-sum solution line by line:

    python
    def two_sum(lst, target):
        # Initialize an empty dictionary to store numbers we've seen and their indices
        value_to_index = {}

        # Loop through each number in the list along with its index
        for i, num in enumerate(lst):
            # Calculate what number we need to find in our dictionary to reach the target
            complement = target - num

            # Check if we've already seen the complement number
            if complement in value_to_index:
                # If found, return the current index and the stored index of the complement
                return (value_to_index[complement], i)

            # If not found, store the current number and its index in the dictionary
            value_to_index[num] = i

        # This line is a safety net (though problem states a solution exists)
        return (-1, -1)
    Example Walkthrough: For
    two_sum([2, 7, 11, 15], 9)
    :

    First iteration (i=0, num=2):
    complement = 9 - 2 = 7
    7 not in dictionary
    Store {2: 0}
    Second iteration (i=1, num=7):
    complement = 9 - 7 = 2
    2 is in dictionary (value is 0)
    Return (0, 1)
    The algorithm efficiently finds the solution in O(n) time with O(n) space complexity by trading space for speed using a hash map.


"""