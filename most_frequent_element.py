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