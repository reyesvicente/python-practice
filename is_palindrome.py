# ============================================================================
# PROBLEM 2: Palindrome Checker
# ============================================================================
# Write a function that checks if a string is a palindrome (reads the same
# forwards and backwards). Ignore spaces and case.
# Example: is_palindrome("racecar") should return True
# Example: is_palindrome("A man a plan a canal Panama") should return True
# Example: is_palindrome("hello") should return False

def is_palindrome(s):
    """
        PSEUDO CODE:
        # Step 1: Convert the string to lowercase to make the check case-insensitive
        # Step 2: Remove all spaces from the string
        # Step 3: Compare the cleaned string with its reverse
        # Step 4: Return True if they match, False otherwise
        cleaned = remove_all_spaces(convert_to_lowercase(s))
        RETURN cleaned == reverse_string(cleaned)
    """
    s = str.lower(s)
    s = s.replace(" ", "")
    return s == s[::-1]

print(is_palindrome("wilabaliw"))

"""
    Let me break down the code line by line:

    Function Definition:
    python
    def is_palindrome(s):
    Defines a function named
    is_palindrome
    that takes one parameter s (the string to check).
    Docstring:
    python
        PSEUDO CODE:
        # Step 1: Convert the string to lowercase to make the check case-insensitive
        # Step 2: Remove all spaces from the string
        # Step 3: Compare the cleaned string with its reverse
        # Step 4: Return True if they match, False otherwise
        cleaned = remove_all_spaces(convert_to_lowercase(s))
        RETURN cleaned == reverse_string(cleaned)
    A multi-line string that documents the function's purpose and logic.
    The pseudo code shows the step-by-step approach to solve the problem.
    Convert to Lowercase:
    python
    s = str.lower(s)
    Converts the entire string to lowercase to make the palindrome check case-insensitive.
    Example: "RaceCar" becomes "racecar".
    Remove Spaces:
    python
    s = s.replace(" ", "")
    Removes all spaces from the string to ignore them in the palindrome check.
    Example: "a man a plan" becomes "amanaplan".
    Palindrome Check:
    python
    return s == s[::-1]
    s[::-1] creates a reversed copy of the string.
    == compares the original string with its reversed version.
    Returns True if they match (palindrome), False otherwise.
    Example: "racecar" == "racecar"[::-1] → True.
    Test Case:
    python
    print(is_palindrome("wilabaliw"))
    Tests the function with the string "wilabaliw", which is a palindrome.
    Expected output: True.
    The code is well-structured and handles all the requirements:

    Case insensitivity
    Space ignoring
    Efficient string reversal using slicing
    Clean and readable implementation
    Feedback submitted
"""