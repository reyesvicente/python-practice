# ============================================================================
# PROBLEM 18: Group Anagrams
# ============================================================================
# Write a function that groups words that are anagrams of each other.
# Return a list of lists where each sublist contains anagrams.
# Example: group_anagrams(['listen', 'silent', 'hello', 'world', 'enlist'])
#          should return [['listen', 'silent', 'enlist'], ['hello'], ['world']]

def group_anagrams(words):
    """
        PSEUDO CODE:
        function group_anagrams(words):
        # Edge case: if input list is empty
        if words is empty:
            return empty list

        # Create a dictionary to store groups of anagrams
        # Key: sorted tuple of characters
        # Value: list of words that are anagrams
        anagram_groups = {}

        # Iterate through each word in the input list
        for word in words:
            # Convert word to lowercase and sort its characters to form a key
            # Using tuple(sorted(word.lower())) for immutability and case-insensitive comparison
            key = sort word's characters and convert to tuple

            # If key exists in dictionary, append the word to its group
            if key exists in anagram_groups:
                append word to anagram_groups[key]
            # Otherwise, create a new entry with this word as the first element
            else:
                anagram_groups[key] = [word]

        # Return all the groups as a list of lists
        return list of values from anagram_groups
    """
    if words is None or len(words) == 0:
        return []

    anagram_groups = {}
    for word in words:
        key = tuple(sorted(word.lower()))

        if key in anagram_groups:
            anagram_groups[key].append(word)
        else:
            anagram_groups[key] = [word]

    return list(anagram_groups.values())


print(group_anagrams(['listen', 'silent', 'hello', 'world', 'enlist']))
print(group_anagrams(['listen', 'silent', 'hello', 'world', 'enlist', 'elbow', 'below']))

"""
    Let me break down the code for you:

    python
    def group_anagrams(words):
        # Handle edge case: if input is None or empty list
        if words is None or len(words) == 0:
            return []  # Return empty list for invalid input

        # Initialize an empty dictionary to store groups of anagrams
        # Key: sorted tuple of characters (acts as a unique identifier for anagrams)
        # Value: list of words that are anagrams of each other
        anagram_groups = {}

        # Process each word in the input list
        for word in words:
            # Create a key by:
            # 1. Converting word to lowercase (for case-insensitive comparison)
            # 2. Sorting the characters (anagrams will have the same sorted characters)
            # 3. Converting to tuple (which is hashable and can be used as a dictionary key)
            key = tuple(sorted(word.lower()))

            # Check if we've seen this anagram group before
            if key in anagram_groups:
                # If yes, append the current word to its group
                anagram_groups[key].append(word)
            else:
                # If not, create a new entry with this word as the first element
                anagram_groups[key] = [word]

        # Return all the groups as a list of lists
        # .values() returns all the lists of anagrams from the dictionary
        return list(anagram_groups.values())
    Example Walkthrough:
    For input ['listen', 'silent', 'hello', 'world', 'enlist']:

    'listen' → key: ('e','i','l','n','s','t') → New group
    'silent' → same key → Added to same group
    'hello' → new key → New group
    'world' → new key → New group
    'enlist' → same key as first group → Added there
    Final result: [['listen', 'silent', 'enlist'], ['hello'], ['world']]
"""