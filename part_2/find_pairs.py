# ============================================================================
# PROBLEM 19: Find Pairs with Target Sum
# ============================================================================
# Write a function that finds all pairs of numbers in a list that add up to a target sum.
# Return a list of tuples. Each pair should only appear once.
# Example: find_pairs([1, 5, 7, -1, 5], 6) should return [(1, 5), (7, -1)]
# Example: find_pairs([2, 3, 4, 5], 9) should return [(4, 5)]

def find_pairs(lst, target):
    """
        PSUEDO CODE:
        1. Initialize an empty set to store unique numbers
        2. Initialize an empty list to store pairs
        3. Iterate through the list
        4. For each number, calculate the complement (target - number)
        5. If the complement is in the set, add the pair to the list
        6. Add the number to the set
        7. Return the list of pairs
    """
    seen = set()
    pairs_found = set()
    for num in lst:
        complement = target - num
        if complement in seen:
            pairs_found.add((min(num, complement), max(num, complement)))
        seen.add(num)
    return list(pairs_found)

print(find_pairs([1, 5, 7, -1, 5], 6))
print(find_pairs([2, 3, 4, 5], 9))


"""
Here's a line-by-line explanation of the
find_pairs
 function:

python
def find_pairs(lst, target):
    # Initialize a set to keep track of numbers we've seen so far
    seen = set()
    # Initialize a set to store unique pairs that sum to target
    pairs_found = set()

    # Loop through each number in the input list
    for num in lst:
        # Calculate what number would pair with current num to make the target sum
        complement = target - num

        # Check if we've seen the complement number before
        if complement in seen:
            # If yes, add the sorted pair to our results to ensure uniqueness
            pairs_found.add((min(num, complement), max(num, complement)))

        # Add current number to our seen set for future iterations
        seen.add(num)

    # Convert the set of tuples to a list before returning
    return list(pairs_found)
Key Points:
seen set: Tracks numbers we've already processed to find pairs efficiently.
pairs_found set: Ensures each pair is only stored once, even if found multiple times.
Complement calculation: For each number, we calculate what other number would make the target sum.
Sorted pairs: Using min and max ensures (a,b) and (b,a) are stored the same way.
O(n) time complexity: Each number is processed exactly once, making it very efficient.
Space complexity: O(n) in the worst case, as we might store all numbers in the seen set.
The test cases show it works correctly:

[1, 5, 7, -1, 5] with target 6 → [(-1, 7), (1, 5)]
[2, 3, 4, 5] with target 9 → [(4, 5)]
"""