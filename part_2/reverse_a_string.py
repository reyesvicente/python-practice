# ============================================================================
# PROBLEM 12: Reverse a String
# ============================================================================
# Write a function that reverses a string without using slicing ([::-1]).
# Example: reverse_string("hello") should return "olleh"
# Example: reverse_string("Python") should return "nohtyP"

def reverse_string(s):
    """
        PSEUDO CODE:
        FUNCTION reverse_string(s):
        reversed_str = empty string
        FOR i FROM length of s - 1 DOWN TO 0:
            reversed_str = reversed_str + s[i]
        RETURN reversed_str
    """
    reversed_str = ""
    for i in range(len(s)-1, -1, -1):
        reversed_str = reversed_str + s[i]
    return reversed_str

print(reverse_string("hello"))
print(reverse_string("Python"))


"""
    Let me break down the code line by line:

    python
    def reverse_string(s):
    Defines a function named
    reverse_string
    that takes a string s as input.
    python
        reversed_str = ""
    Initializes an empty string reversed_str to store the reversed string.
    python
        for i in range(len(s)-1, -1, -1):
    Starts a loop that goes from the last index of the string to the first.
    len(s)-1 is the last index (since Python is 0-based).
    -1 is the stop value (exclusive), so we go down to 0.
    The third -1 means we're counting down.
    python
            reversed_str = reversed_str + s[i]
    In each iteration, we take the character at position i from the original string.
    Append it to reversed_str.
    This builds the reversed string one character at a time.
    python
        return reversed_str
    Returns the fully reversed string.
    python
    print(reverse_string("hello"))  # Output: "olleh"
    print(reverse_string("Python"))  # Output: "nohtyP"
    Test cases that demonstrate the function works correctly.
    For example, with "hello":

    i=4: reversed_str = "" + "o" = "o"
    i=3: reversed_str = "o" + "l" = "ol"
    i=2: reversed_str = "ol" + "l" = "oll"
    i=1: reversed_str = "oll" + "e" = "olle"
    i=0: reversed_str = "olle" + "h" = "olleh"
"""