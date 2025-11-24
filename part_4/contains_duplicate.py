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


"""
Line-by-Line Explanation
def contains_duplicate(lst):
Defines a new function named
contains_duplicate
 that accepts one parameter, lst (the list of numbers to check).
seen = set()
Initializes an empty set named seen.
Why a set? Sets are hash-based structures, making lookups (checking if an item exists) extremely fast—on average O(1) time complexity—compared to lists which are O(n).
for num in lst:
Starts a loop that iterates through every element in the input list lst, assigning the current element to the variable num one by one.
if num in seen:
Checks if the current number (num) is already present in the seen set. This is the core check for duplicates.
return True
If the condition above is true (the number was seen before), the function immediately stops and returns True, indicating a duplicate was found.
seen.add(num)
If the number was not in the set, this line adds it to seen. This effectively "remembers" the number for future iterations.
return False
This line is only reached if the loop finishes completely without finding any duplicates. It returns False to indicate all elements are unique.
print(contains_duplicate([1, 2, 3, 1]))
Calls the function with [1, 2, 3, 1]. Since 1 appears twice, the function returns True, which is then printed.
print(contains_duplicate([1, 2, 3, 4]))
Calls the function with [1, 2, 3, 4]. Since all numbers are unique, the function returns False, which is then printed.
Complexity Analysis
Time Complexity: O(n) — We iterate through the list at most once.

"""