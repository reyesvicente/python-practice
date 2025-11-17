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
    count = {}
    for num in lst:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    total = 0
    for num, cnt in count.items():
        if cnt == 1:
            total += num

    return total

print(sum_of_unique([1, 2, 2, 3, 3, 3]))
print(sum_of_unique([1, 1, 1, 1]))
print(sum_of_unique([5, 4, 3, 2, 1]))