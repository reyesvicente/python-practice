# ============================================================================
# PROBLEM 9: Most Frequent Element
# ============================================================================
# Write a function that finds the most frequently occurring element in a list.
# Example: most_frequent([1, 1, 1, 2, 2, 3]) should return 1
# Example: most_frequent(['a', 'b', 'b', 'c']) should return 'b'

def most_frequent(lst):
    """
        PSEUDO CODE
        // Handle empty list case
        IF lst is empty:
            RETURN None or raise an error

        // Create a dictionary to store frequency of each element
        frequency = empty dictionary

        // Count frequency of each element
        FOR EACH element IN lst:
            IF element is in frequency:
                INCREMENT frequency[element] by 1
            ELSE:
                SET frequency[element] = 1

        // Find the element with maximum frequency
        max_count = 0
        most_frequent_element = None

        FOR EACH element, count IN frequency.items():
            IF count > max_count:
                max_count = count
                most_frequent_element = element
            // In case of tie, this will keep the first one encountered
            // For handling ties differently, we'd need to modify this part

        RETURN most_frequent_element
    """
    if len(lst) == 0:
        return None

    frequency = {}
    for element in lst:
        if element in frequency:
            frequency[element] += 1
        else:
            frequency[element] = 1
    max_count = 0
    most_frequent_element = None

    for element, count in frequency.items():
        if count > max_count:
            max_count = count
            most_frequent_element = element
    return most_frequent_element


print(most_frequent([1, 1, 1, 2, 2, 3]))
print(most_frequent(['a', 'b', 'b', 'c']))
print(most_frequent([5, 5, 6, 1, 3, 32]))


"""
    Let me break down the code line by line, excluding the pseudo code:

    python
    def most_frequent(lst):
        # Check if the input list is empty
        if len(lst) == 0:
            return None  # Return None if the list is empty

        # Initialize an empty dictionary to store element frequencies
        frequency = {}

        # Count how many times each element appears in the list
        for element in lst:
            # If the element is already in the dictionary, increment its count
            if element in frequency:
                frequency[element] += 1
            # If the element is not in the dictionary, add it with a count of 1
            else:
                frequency[element] = 1

        # Initialize variables to track the most frequent element
        max_count = 0
        most_frequent_element = None

        # Find the element with the highest frequency
        for element, count in frequency.items():
            # If current element's count is greater than the current max
            if count > max_count:
                max_count = count  # Update the max count
                most_frequent_element = element  # Update the most frequent element

        # Return the most frequently occurring element
        return most_frequent_element

    # Test cases
    print(most_frequent([1, 1, 1, 2, 2, 3]))  # Output: 1
    print(most_frequent(['a', 'b', 'b', 'c']))  # Output: 'b'
    print(most_frequent([5, 5, 6, 1, 3, 32]))  # Output: 5
    Key Points:
    Edge Case Handling: The function first checks if the input list is empty.
    Frequency Dictionary: Uses a dictionary to count occurrences of each element.
    Finding the Most Frequent: Iterates through the dictionary to find the element with the highest count.
    Tie Handling: In case of ties, it returns the first element encountered with the highest frequency.
    The test cases at the bottom demonstrate the function's behavior with different types of input lists.
"""