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