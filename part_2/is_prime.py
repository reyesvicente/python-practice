# ============================================================================
# PROBLEM 11: Check if a Number is Prime
# ============================================================================
# Write a function that checks if a number is prime.
# A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
# Example: is_prime(7) should return True
# Example: is_prime(10) should return False
# Example: is_prime(2) should return True

def is_prime(n):
    """
        IF n <= 1:
        RETURN False
        IF n == 2:
            RETURN True
        IF n is even:
            RETURN False

        # Check for divisors up to square root of n
        FOR i FROM 3 TO SQUARE_ROOT(n) STEP 2:
            IF n % i == 0:
                RETURN False
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

print(is_prime(7))
print(is_prime(10))
print(is_prime(2))

"""
    Let's break down the
    is_prime
    function line by line:

    python
    def is_prime(n):
        # Check if n is less than or equal to 1
        # Numbers ≤ 1 are not prime by definition
        if n <= 1:
            return False

        # 2 is the only even prime number
        if n == 2:
            return True

        # Check if n is even (and not 2)
        if n % 2 == 0:
            return False

        # Check odd divisors from 3 up to the square root of n
        # We use int(n**0.5) + 1 because:
        # 1. n**0.5 is the square root of n
        # 2. We convert to int to get a whole number
        # 3. Add 1 because range is exclusive of the end value
        # We step by 2 to only check odd numbers
        for i in range(3, int(n**0.5) + 1, 2):
            # If n is divisible by any number in this range, it's not prime
            if n % i == 0:
                return False

        # If we get here, n is prime
        return True
    Test Cases:
    python
    print(is_prime(7))   # True (7 is prime)
    print(is_prime(10))  # False (10 is divisible by 2 and 5)
    print(is_prime(2))   # True (2 is the only even prime)
    Key Optimizations:
    Early Returns: We return False as soon as we find a divisor
    Reduced Search Space: Only check up to the square root of n
    Skip Even Numbers: After checking 2, we can skip all other even numbers
    The function efficiently determines if a number is prime with minimal computations.
"""