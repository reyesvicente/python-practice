# ============================================================================
# PROBLEM 7: Factorial
# ============================================================================
# Write a function that calculates the factorial of a number.
# Factorial of n (n!) = n × (n-1) × (n-2) × ... × 1
# Example: factorial(5) should return 120 (5 × 4 × 3 × 2 × 1)
# Example: factorial(0) should return 1

def factorial(n):
    """
        PSEUDO CODE:
            IF n is 0 OR n is 1:
            RETURN 1
        ELSE:
            result = 1
            FOR i FROM 2 TO n:
                result = result * i
            RETURN result
    """
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

print(factorial(5))
print(factorial(0))
print(factorial(7))


"""
    EXPLANATION
    Let me break down the code line by line:

    python
    def factorial(n):
    Defines a function named
    factorial
    that takes one parameter n (the number to calculate factorial for).
    python
        PSEUDO CODE:
            IF n is 0 OR n is 1:
            RETURN 1
        ELSE:
            result = 1
            FOR i FROM 2 TO n:
                result = result * i
            RETURN result
    This is a docstring (multi-line comment) showing the pseudo code that was used to design the function.
    python
        if n == 0 or n == 1:
            return 1
    Base case: If n is 0 or 1, return 1 immediately since 0! and 1! both equal 1.
    python
        else:
            result = 1
    If n is greater than 1, initialize result to 1 (the multiplicative identity).
    python
            for i in range(2, n + 1):
                result *= i
    Loop from 2 to n (inclusive). In each iteration, multiply result by the current number i.
    For example, if n is 5:
    First iteration: result = 1 * 2 = 2
    Second: result = 2 * 3 = 6
    Third: result = 6 * 4 = 24
    Fourth: result = 24 * 5 = 120
    python
            return result
    Return the final computed factorial value.
    python
    print(factorial(5))  # Output: 120 (5! = 5*4*3*2*1 = 120)
    print(factorial(0))  # Output: 1 (0! is defined as 1)
    print(factorial(7))  # Output: 5040 (7! = 7*6*5*4*3*2*1 = 5040)
    Test cases showing the function in action with different inputs.
"""