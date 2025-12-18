# ============================================================================
# PROBLEM 40: Maximum Subarray Sum
# ============================================================================
# Write a function that finds the contiguous subarray with the largest sum.
# Return the maximum sum. (Kadane's Algorithm)
# Example: max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) should return 6 (subarray [4, -1, 2, 1])
# Example: max_subarray_sum([-1]) should return -1

def max_subarray_sum(lst):
    """
    Finds the contiguous subarray with the largest sum using Kadane's Algorithm.

    Pseudocode:
    FUNCTION max_subarray_sum(lst):
        IF lst is empty:
            RETURN 0

        INITIALIZE current_sum = 0
        INITIALIZE max_sum = negative infinity (or first element of lst)

        FOR EACH number in lst:
            current_sum = current_sum + number
            IF current_sum > max_sum:
                max_sum = current_sum
            IF current_sum < 0:
                current_sum = 0

        RETURN max_sum
    """
    if lst is None:
        return 0

    current_sum = 0
    max_sum = lst[0]

    for num in lst:
        current_sum += num
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0

    return max_sum

print(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_subarray_sum([-1]))