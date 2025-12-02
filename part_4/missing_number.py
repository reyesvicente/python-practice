# ============================================================================
# PROBLEM 35: Missing Number in Range
# ============================================================================
# Write a function that finds the missing number in a list containing numbers from 1 to n.
# The list is unsorted and may have duplicates. Find any missing number.
# Example: missing_number([1, 2, 4, 5]) should return 3
# Example: missing_number([3, 1, 2, 4, 5, 6, 8]) should return 7

def missing_number(lst):
    """
    PSEUDOCODE:
    1. If the list is empty, return 1.
    2. Convert the list to a set `num_set` to remove duplicates and enable O(1) lookups.
    3. Find the maximum value in the list, let's call it `max_val`.
    4. Iterate through numbers `i` from 1 to `max_val`:
        a. If `i` is not in `num_set`:
            - Return `i` (found the missing number).
    5. If the loop finishes without returning:
        - Return `max_val + 1` (the sequence is complete up to max_val, so the next missing is max_val + 1).
    """
    if lst is None or len(lst) == 0:
        return 1
    num_set = set(lst)
    max_val = max(num_set)
    for i in range(1, max_val + 1):
        if i not in num_set:
            return i
    return max_val + 1

print(missing_number([1, 2, 4, 5]))
print(missing_number([3, 1, 2, 4, 5, 6, 8]))

"""
Here is the line-by-line explanation of your
missing_number
 function:

Function Definition
python
def missing_number(lst):
Defines the function named
missing_number
 that accepts one argument, lst (the list of numbers).
Edge Case Handling
python
    if lst is None or len(lst) == 0:
        return 1
Check: Checks if the list is None (doesn't exist) or if its length is 0 (empty).
Action: If either is true, it returns 1. This handles the case where there are no numbers, so the first missing number is naturally 1.
Optimization (Set Conversion)
python
    num_set = set(lst)
Converts the list lst into a set called num_set.
Why?
Removes Duplicates: The problem states the list "may have duplicates." Sets automatically remove them.
Speed: Checking if a number is inside a list is slow (O(N)), but checking if it's inside a set is extremely fast (O(1)).
Finding the Range
python
    max_val = max(num_set)
Finds the largest number in the set. This helps define the upper limit of the range we need to check (from 1 to max_val).
The Search Loop
python
    for i in range(1, max_val + 1):
Starts a loop from 1 up to max_val.
Note: range(1, max_val + 1) stops before the second argument, so it effectively loops from 1 to max_val inclusive.
python
        if i not in num_set:
            return i
Check: For every number i in that sequence, it asks: "Is this number inside our set?"
Action: If i is not found, it means i is the missing number. The function immediately returns i and stops.
Fallback Return
python
    return max_val + 1
If the loop finishes without returning anything, it means every number from 1 to max_val was present.
Therefore, the missing number must be the next number in the sequence, which is max_val + 1.
Example: If the input is [1, 2, 3], the loop finds 1, 2, and 3. It finishes, and the function returns 4.
"""
