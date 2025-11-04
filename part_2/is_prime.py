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