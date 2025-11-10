# ============================================================================
# PROBLEM 21: Is Anagram
# ============================================================================
# Write a function that checks if two strings are anagrams of each other.
# Anagrams are words that contain the same letters in a different order.
# Ignore spaces and case.
# Example: is_anagram("listen", "silent") should return True
# Example: is_anagram("hello", "world") should return False
# Example: is_anagram("The Eyes", "They See") should return True

def is_anagram(s1, s2):
    """
      PSEUDO CODE:
      1. Remove spaces and convert to lowercase
      2. Check if the sorted characters of both strings are equal
      3. Return True if they are equal, False otherwise
    """
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    return sorted(s1) == sorted(s2)

print(is_anagram("listen", "silent"))
print(is_anagram("hello", "world"))
print(is_anagram("The Eyes", "They See"))

"""
  Let me break down the code line by line:

  python
  # Function definition that takes two strings as input
  def is_anagram(s1, s2):
      # Remove all spaces from s1 and convert to lowercase
      s1 = s1.replace(" ", "").lower()
      # Remove all spaces from s2 and convert to lowercase
      s2 = s2.replace(" ", "").lower()

      # Sort characters of both strings and compare them
      # Returns True if they are anagrams, False otherwise
      return sorted(s1) == sorted(s2)

  # Test cases
  print(is_anagram("listen", "silent"))  # True - same letters in different order
  print(is_anagram("hello", "world"))    # False - different sets of letters
  print(is_anagram("The Eyes", "They See"))  # True - same letters, ignoring case and spaces
  How it works:
  The function takes two strings s1 and s2.
  For each string:
  replace(" ", "") removes all spaces
  lower() converts all characters to lowercase
  sorted() converts each string into a list of its characters, sorted alphabetically
  The function returns True if the sorted lists are identical (meaning they contain the same characters in the same frequency), False otherwise
  The test cases demonstrate:

  "listen" and "silent" are anagrams
  "hello" and "world" are not anagrams
  "The Eyes" and "They See" are anagrams when ignoring case and spaces
"""