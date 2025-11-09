# ============================================================================
# PROBLEM 20: Longest Common Prefix
# ============================================================================
# Write a function that finds the longest common prefix among a list of strings.
# Example: longest_common_prefix(['flower', 'flow', 'flight']) should return 'fl'
# Example: longest_common_prefix(['dog', 'racecar', 'car']) should return ''
# Example: longest_common_prefix(['interspecies', 'interstellar']) should return 'inters'

def longest_common_prefix(strings):
    """
        PSEUDO CODE:
            function longest_common_prefix(strings):
            if strings is empty:
                return empty string

            set prefix to the first string in strings

            for each string s in strings starting from the second string:
                while s does not start with prefix:
                    remove the last character from prefix
                    if prefix is empty:
                        return empty string

            return prefix
    """
    if strings is None or strings == 0:
        return ""

    prefix = strings[0]
    for s in strings[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if prefix == "":
                return ""
    return prefix

print(longest_common_prefix(['flower', 'flow', 'flight']))
print(longest_common_prefix(['dog', 'racecar', 'car']))
print(longest_common_prefix(['interspecies', 'interstellar']))


"""
    Let me explain the code line by line:

    if strings is None or strings == 0: - Checks if the input list is None or 0 (though strings == 0 might be a bug - it should be not strings to check for empty list)
        return "" - Returns an empty string if the input is invalid
    prefix = strings[0] - Takes the first string in the list as the initial prefix
    for s in strings[1:]: - Iterates through each remaining string in the list
    strings[1:] means "all elements from index 1 to the end"
        while not s.startswith(prefix): - Keeps running as long as the current string doesn't start with the current prefix
    s.startswith(prefix) checks if string s begins with the prefix
            prefix = prefix[:-1] - Removes the last character from the prefix
    prefix[:-1] is string slicing that takes all characters except the last one
            if prefix == "": - If we've removed all characters from the prefix
        return "" - Return empty string as there's no common prefix
    return prefix - If we've checked all strings, return the longest common prefix found
    The algorithm works by:

    Starting with the first string as the initial prefix
    For each subsequent string, it shortens the prefix from the end until it matches the start of that string
    If the prefix becomes empty at any point, we know there's no common prefix
    The remaining prefix after checking all strings is the longest common prefix
    Example with ['flower', 'flow', 'flight']:

    Start with prefix = 'flower'
    Compare with 'flow':
    'flow' doesn't start with 'flower' → remove last character → 'flowe'
    'flow' doesn't start with 'flowe' → remove last character → 'flow'
    'flow' starts with 'flow' → keep prefix as 'flow'
    Compare with 'flight':
    'flight' doesn't start with 'flow' → remove last character → 'flo'
    'flight' doesn't start with 'flo' → remove last character → 'fl'
    'flight' starts with 'fl' → keep prefix as 'fl'
    Return 'fl' as the longest common prefix
"""