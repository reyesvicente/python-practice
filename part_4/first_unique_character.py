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
