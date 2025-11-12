# ============================================================================
# PROBLEM 25: String Compression
# ============================================================================
# Write a function that compresses a string by counting consecutive characters.
# If the compressed string is not shorter than the original, return the original.
# Example: compress_string("abcccccaab") should return "a1b1c5a2b1"
# Example: compress_string("abc") should return "abc"
# Example: compress_string("aaaa") should return "a4"

# ============================================================================
# PROBLEM 25: String Compression
# ============================================================================
def compress_string(s):
    """
        FUNCTION compress_string(s):
            // Handle empty or None strings
            IF s is None OR length of s is 0:
                RETURN s

            // Initialize variables
            compressed = empty string
            count = 1
            current_char = first character of s

            // Iterate through the string starting from the second character
            FOR i from 1 to length of s - 1:
                IF s[i] equals current_char:
                    INCREMENT count by 1
                ELSE:
                    // Add current character and its count to compressed string
                    APPEND current_char and count to compressed
                    SET current_char to s[i]
                    RESET count to 1

            // Add the last character and its count
            APPEND current_char and count to compressed

            // Return the shorter string
            IF length of compressed <= length of s:
                RETURN compressed
            ELSE:
                RETURN s
        END FUNCTION
    """
    # Handle empty or None strings
    if s is None or len(s) == 0:
        return s

    compressed = ""
    count = 1
    current_char = s[0]

    # Iterate through the string starting from the second character
    for i in range(1, len(s)):
        if s[i] == current_char:
            count += 1
        else:
            # Append current character and its count to compressed string
            compressed += current_char + str(count)
            current_char = s[i]
            count = 1

    # Add the last character and its count
    compressed += current_char + str(count)

    # Return the shorter string
    if len(compressed) <= len(s):
        return compressed
    else:
        return s


# Test cases
print(compress_string("abcccccaab"))  # Expected: a1b1c5a2b1
print(compress_string("abc"))         # Expected: abc
print(compress_string("aaaa"))        # Expected: a4

"""
    Let me break down the code line by line:

    python
    def compress_string(s):
        Function documentation with pseudo code
        # Handle empty or None strings
        if s is None or len(s) == 0:  # Check if input is None or empty
            return s                   # Return as-is if empty or None

        compressed = ""               # Initialize empty string to store compressed result
        count = 1                     # Initialize counter for current character
        current_char = s[0]           # Store first character to start comparison

        # Iterate through the string starting from the second character
        for i in range(1, len(s)):    # Loop from index 1 to end of string
            if s[i] == current_char:  # If current character matches previous
                count += 1            # Increment the counter
            else:
                # If character changes, append previous character and its count
                compressed += current_char + str(count)
                current_char = s[i]   # Update current character to new character
                count = 1             # Reset counter for new character

        # After loop ends, add the last character and its count
        compressed += current_char + str(count)

        # Return the shorter string (compressed or original)
        if len(compressed) <= len(s):  # If compressed isn't longer than original
            return compressed          # Return compressed version
        else:
            return s                   # Otherwise return original string
    Example Walkthrough:
    For input "abcccccaab":

    Starts with 'a', count=1
    Next 'b' is different → append 'a1'
    'b' count=1, next 'c' is different → append 'b1'
    'c' count starts at 1, increments to 5 → append 'c5'
    'a' count=2 → append 'a2'
    'b' count=1 → append 'b1'
    Final compressed: "a1b1c5a2b1" (10 chars) vs original (9 chars) → returns original
    For input "abc":

    Compressed would be "a1b1c1" (6 chars) vs original (3 chars) → returns original "abc"
    For input "aaaa":

    Compressed is "a4" (2 chars) vs original (4 chars) → returns "a4"
"""