# ============================================================================
# PROBLEM 1: Sum of Digits
# ============================================================================
# Write a function that takes an integer and returns the sum of its digits.
# Example: sum_of_digits(123) should return 6 (1 + 2 + 3)
# Example: sum_of_digits(9999) should return 36

def sum_of_digits(n):
    """
        PSEUDO CODE:
        1. Initialize a variable to store the sum of digits (e.g., sum = 0)
        2. Use a loop to iterate through each digit of the number
        3. Convert the number to a string to access each digit
        4. Convert each digit back to an integer and add it to the sum
        5. Return the sum of the digits
    """
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum


print(sum_of_digits(144))
print(sum_of_digits(9999))