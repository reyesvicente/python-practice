# ============================================================================
# PROBLEM 3: Find Missing Number
# ============================================================================
# Given a list of numbers from 1 to n with one number missing,
# find the missing number.
# Example: find_missing([1, 2, 3, 5]) should return 4
# Example: find_missing([1, 3, 4, 5]) should return 2

def find_missing(numbers):
    """
        PSEUDO CODE:
        # Step 1: Calculate the expected sum of numbers from 1 to n
        # (n is the length of the list + 1 since one number is missing)
        n = length of numbers + 1
        expected_sum = (n * (n + 1)) // 2  # Formula for sum of first n natural numbers

        # Step 2: Calculate the actual sum of numbers in the list
        actual_sum = sum of all numbers in the list

        # Step 3: The missing number is the difference between expected and actual sum
        missing_number = expected_sum - actual_sum

        # Step 4: Return the missing number
        RETURN missing_number
    """
    n = len(numbers) + 1
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(numbers)
    missing_number = expected_sum - actual_sum
    return missing_number

print(find_missing([1, 2, 3, 5]))
print(find_missing([1, 3, 4, 5]))


"""
    Let me break down the code for you:

    Function Definition:
    python
    def find_missing(numbers):
    Defines a function called
    find_missing
    that takes a list of numbers as input.
    Docstring:
    python
    PSEUDO CODE:
    # Step 1: Calculate the expected sum of numbers from 1 to n
    # (n is the length of the list + 1 since one number is missing)
    n = length of numbers + 1
    expected_sum = (n * (n + 1)) // 2  # Formula for sum of first n natural numbers

    # Step 2: Calculate the actual sum of numbers in the list
    actual_sum = sum of all numbers in the list

    # Step 3: The missing number is the difference between expected and actual sum
    missing_number = expected_sum - actual_sum

    # Step 4: Return the missing number
    RETURN missing_number
    This is a multi-line comment that explains the logic using pseudo-code.
    Calculate n:
    python
    n = len(numbers) + 1
    len(numbers) gives the length of the input list.
    We add 1 because one number is missing from the sequence.
    Calculate Expected Sum:
    python
    expected_sum = (n * (n + 1)) // 2
    Uses the formula for the sum of the first n natural numbers: n*(n+1)/2
    Example: For n=5, expected_sum = (5*6)/2 = 15 (1+2+3+4+5)
    Calculate Actual Sum:
    python
    actual_sum = sum(numbers)
    Calculates the sum of all numbers in the input list.
    Find Missing Number:
    python
    missing_number = expected_sum - actual_sum
    The difference between the expected sum and actual sum gives the missing number.
    Return Result:
    python
    return missing_number
    Returns the calculated missing number.
    Example: For
    find_missing([1, 2, 3, 5])
    :

    n = 4 + 1 = 5
    expected_sum = (5 * 6) // 2 = 15
    actual_sum = 1 + 2 + 3 + 5 = 11
    missing_number = 15 - 11 = 4
    The code is efficient with O(n) time complexity (due to the sum operation) and O(1) space complexity.
"""