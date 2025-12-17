# ============================================================================
# PROBLEM 36: Majority Element
# ============================================================================
# Write a function that finds the majority element in a list.
# The majority element is the element that appears more than n/2 times.
# Assume a majority element always exists.
# Example: majority_element([3, 2, 3]) should return 3
# Example: majority_element([2, 2, 1, 1, 1, 2, 2]) should return 2

def majority_element(lst):
    # Pseudo Code (Boyer-Moore Voting Algorithm):
    # 1. Initialize a candidate variable to None and a counter to 0.
    # 2. Iterate through each element in the list:
    #    a. If the counter is 0, pick the current element as the new candidate.
    #    b. If the current element matches the candidate, increment the counter.
    #    c. If the current element does not match, decrement the counter.
    # 3. Return the candidate (since a majority element always exists).
    candidate = None
    count = 0

    for num in lst:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    return candidate

print(majority_element([3, 2, 3]) )
print(majority_element([2, 2, 1, 1, 1, 2, 2]))