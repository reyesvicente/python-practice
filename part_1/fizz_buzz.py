# ============================================================================
# PROBLEM 8: FizzBuzz
# ============================================================================
# Write a function that prints numbers 1 to n, but:
# - For multiples of 3, print "Fizz"
# - For multiples of 5, print "Buzz"
# - For multiples of both, print "FizzBuzz"
# Return a list of the results.
# Example: fizzbuzz(15) should return [1, 2, 'Fizz', 4, 'Buzz', ...]

def fizzbuzz(n):
    """
        PSEUDO CODE:
        results = empty list

        for i from 1 to n (inclusive):
            if i is divisible by both 3 and 5:
                append "FizzBuzz" to results
            else if i is divisible by 3:
                append "Fizz" to results
            else if i is divisible by 5:
                append "Buzz" to results
            else:
                append i to results
    """
    results = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            results.append("FizzBuzz")
        else:
            if i % 3 == 0:
                results.append("Fizz")
            elif i % 5 == 0:
                results.append("Buzz")
            else:
                results.append(i)
    return results


print(fizzbuzz(15))


"""
Let me break down the FizzBuzz solution line by line:

python
def fizzbuzz(n):
    # Function definition that takes an integer n as input
    # This will be our upper limit for the FizzBuzz sequence

    results = []
    # Initialize an empty list to store the results

    for i in range(1, n + 1):
        # Loop from 1 to n (inclusive)
        # range(1, n+1) generates numbers from 1 to n

        if i % 3 == 0 and i % 5 == 0:
            # Check if number is divisible by both 3 and 5 (i.e., divisible by 15)
            results.append("FizzBuzz")
            # If yes, add "FizzBuzz" to results

        else:  # If not divisible by both
            if i % 3 == 0:
                # Check if divisible by 3
                results.append("Fizz")
                # If yes, add "Fizz" to results

            elif i % 5 == 0:
                # If not divisible by 3, check if divisible by 5
                results.append("Buzz")
                # If yes, add "Buzz" to results

            else:
                # If not divisible by 3 or 5
                results.append(i)
                # Add the number itself to results

    return results
    # Return the complete list of results
Key points about the implementation:

The order of conditions is important - we check for multiples of 15 (3×5) first, then 3, then 5.
The modulo operator % gives the remainder of division, so i % 3 == 0 checks for divisibility by 3.
The function builds the result list incrementally and returns it at the end.
The time complexity is O(n) since we process each number exactly once.
The space complexity is O(n) to store the results.
"""