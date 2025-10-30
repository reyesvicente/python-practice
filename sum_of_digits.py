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
"""
    Let me explain how this code works and why `split()`` isn't needed:

    The function `sum_of_digits(n)` calculates the sum of all digits in a given number n. Here's how it works:

    `sum = 0` - Initializes a variable to store the running total of the digits.
    `for digit in str(n):` - This line does two things:
    `str(n)` converts the input number to a string, allowing us to iterate over each digit.
    The loop then goes through each character (digit) in this string one by one.
    `sum += int(digit)` - For each digit:
    `int(digit)` converts the string digit back to an integer.
    `+=` adds this integer to our running total.
    Finally, `return sum` gives us the total sum of all digits.
    Why `split()` isn't needed:

    `split()` is used to split strings based on a delimiter (like spaces or commas).
    When you convert a number to a string using `str(n)`, you can directly iterate over its characters without splitting because strings in Python are already sequences of characters.
    For example, if n = 123:

    str(123) gives '123'
    Iterating over '123' gives you '1', '2', '3' in sequence
    Each is converted back to an integer and added to the sum
    The code is already efficient and Pythonic as it is!
"""