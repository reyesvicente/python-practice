# ============================================================================
# PROBLEM 23: Longest Substring Without Repeating Characters
# ============================================================================
# Write a function that finds the length of the longest substring without repeating characters.
# Example: longest_substring("abcabcbb") should return 3 (substring "abc")
# Example: longest_substring("bbbbb") should return 1 (substring "b")
# Example: longest_substring("pwwkew") should return 3 (substring "wke")

def longest_substring(s):
    """
        PSEUDO CODE:
        1. Initialize two pointers, left and right, to the start of the string, respectively.
        2. Initialize a set to store the characters in the current substring.
        3. Initialize a variable to store the maximum length of the substring.
        4. While the right pointer is less than the length of the string:
            a. If the character at the right pointer is not in the set, add it to the set and move the right pointer to the right.
            b. If the character at the right pointer is in the set, remove the character at the left pointer from the set and move the left pointer to the right.
            c. Update the maximum length of the substring.
        5. Return the maximum length of the substring.
    """
    left = 0
    right = 0
    max_length = 0
    char_set = set()
    while right < len(s):
        if s[right] not in char_set:
            char_set.add(s[right])
            right += 1
            max_length = max(max_length, right - left)
        else:
            char_set.remove(s[left])
            left += 1
    return max_length

print(longest_substring("abcabcbb"))
print(longest_substring("bbbbb"))
print(longest_substring("pwwkew"))