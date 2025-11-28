# ============================================================================
# PROBLEM 34: First Unique Character
# ============================================================================
# Write a function that finds the index of the first non-repeating character in a string.
# Return -1 if all characters repeat.
# Example: first_unique_char("leetcode") should return 0 (character 'l')
# Example: first_unique_char("loveleetcode") should return 2 (character 'v')
# Example: first_unique_char("aabb") should return -1

def first_unique_char(s):
    char_counts = {}
    for char in s:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i
    return -1

print(first_unique_char("leetcode"))
print(first_unique_char("loveleetcode"))
print(first_unique_char("aabb"))

"""
Here is the line-by-line explanation for the
first_unique_char
 function:

python
def first_unique_char(s):
Line 10: Defines the function
first_unique_char
 that takes a single argument s, which is the string to be analyzed.

python
    char_counts = {}
Line 11: Initializes an empty dictionary named char_counts. This will be used to store each character from the string as a key and its frequency (how many times it appears) as the value.

python
    for char in s:
Line 12: Starts a loop that iterates through every character
char
 in the input string s.

python
        if char in char_counts:
            char_counts[char] += 1
Lines 13-14: Checks if the current character
char
 is already in the char_counts dictionary. If it is, it increments the count for that character by 1.

python
        else:
            char_counts[char] = 1
Lines 15-16: If the character is not in the dictionary (meaning it's the first time we've seen it), it adds the character to the dictionary with a count of 1.

python
    for i, char in enumerate(s):
Line 17: Starts a second loop through the string s. enumerate(s) provides both the index i (position) and the character
char
 at that position. We need the index because the problem asks us to return the index of the first unique character.

python
        if char_counts[char] == 1:
            return i
Lines 18-19: Checks the dictionary char_counts to see if the count for the current character is exactly 1. If it is, this means it is a unique character. Since we are iterating from the beginning of the string, the first one we find is the first unique character, so we immediately return its index i.

python
    return -1
Line 20: If the loop finishes without returning, it means no character had a count of 1 (all characters repeated). The function returns -1 as required by the problem statement.

python
print(first_unique_char("leetcode"))
print(first_unique_char("loveleetcode"))
print(first_unique_char("aabb"))
Lines 22-24: These lines test the function with the provided examples.

"leetcode" returns 0 ('l' is unique).
"loveleetcode" returns 2 ('v' is the first unique one; 'l' and 'o' repeat).
"aabb" returns -1 (no unique characters).
"""