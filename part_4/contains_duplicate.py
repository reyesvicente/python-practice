# ============================================================================
# PROBLEM 32: Contains Duplicate
# ============================================================================
# Write a function that checks if a list contains duplicate elements.
# Return True if duplicates exist, False otherwise.
# Example: contains_duplicate([1, 2, 3, 1]) should return True
# Example: contains_duplicate([1, 2, 3, 4]) should return False

def contains_duplicate(lst):
    # Initialize an empty set to store seen elements
    # seen = {}

    # Iterate through each number in the input list
    # for num in lst:
        # Check if the number is already in the seen set
        # if num in seen:
            # If it is, we found a duplicate, return True
            # return True

        # Add the number to the seen set
        # seen.add(num)

    # If the loop finishes without returning, no duplicates were found
    # return False
    seen = set()
    for num in lst:
        if num in seen:
            return True
        seen.add(num)
    return False

print(contains_duplicate([1, 2, 3, 1]))
print(contains_duplicate([1, 2, 3, 4]))