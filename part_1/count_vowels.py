# ============================================================================
# PROBLEM 4: Count Vowels
# ============================================================================
# Write a function that counts the number of vowels in a string.
# Example: count_vowels("hello world") should return 3
# Example: count_vowels("AEIOU") should return 5

def count_vowels(s):
    """
        FUNCTION count_vowels(s):
        # Step 1: Define what counts as a vowel (both lowercase and uppercase)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

        # Step 2: Initialize a counter for vowels
        count = 0

        # Step 3: Iterate through each character in the string
        FOR each character IN s:
            # Step 4: Check if the character is a vowel
            IF character IN vowels:
                # Step 5: Increment the counter if it's a vowel
                count = count + 1

        # Step 6: Return the total count of vowels
        RETURN count
    """
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

print(count_vowels("pooopcycle"))


"""
    Let me break down the code line by line:

    Function Definition:
    python
    def count_vowels(s):
    Defines a function named
    count_vowels
    that takes a string s as input.
    Docstring:
    python
    FUNCTION count_vowels(s):
    ...
    RETURN count
    A multi-line string that documents the function's purpose and logic using pseudo-code.
    Vowel Set:
    python
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    Creates a set containing all vowels (both lowercase and uppercase).
    A set is used for O(1) lookup time.
    Counter Initialization:
    python
    count = 0
    Initializes a counter to keep track of the number of vowels found.
    String Iteration:
    python
    for char in s:
    Iterates through each character in the input string s.
    Vowel Check:
    python
    if char in vowels:
    Checks if the current character is in the vowels set.
    Counter Increment:
    python
    count += 1
    If the character is a vowel, increments the counter by 1.
    Return Result:
    python
    return count
    Returns the total count of vowels found in the string.
    Test Case:
    python
    print(count_vowels("pooopcycle"))
    Tests the function with the string "pooopcycle".
    Expected output: 4 (o, o, o, e).
    Key Points:

    Time Complexity: O(n) where n is the length of the string.
    Space Complexity: O(1) for the set of vowels.
    Handles both uppercase and lowercase vowels.
    Efficiently checks for vowel membership using a set.
"""