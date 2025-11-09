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

