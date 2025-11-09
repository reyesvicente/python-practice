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