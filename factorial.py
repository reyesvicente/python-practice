# ============================================================================
# PROBLEM 7: Factorial
# ============================================================================
# Write a function that calculates the factorial of a number.
# Factorial of n (n!) = n × (n-1) × (n-2) × ... × 1
# Example: factorial(5) should return 120 (5 × 4 × 3 × 2 × 1)
# Example: factorial(0) should return 1

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
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

print(factorial(5))
print(factorial(0))
print(factorial(7))