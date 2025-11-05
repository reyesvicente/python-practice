# ============================================================================
# PROBLEM 13: Count Character Frequency
# ============================================================================
# Write a function that returns a dictionary with the frequency of each character in a string.
# Ignore spaces and convert to lowercase.
# Example: char_frequency("hello world") should return {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

def char_frequency(s):
    """
        FUNCTION char_frequency(INPUT string s)
            CREATE empty dictionary freq_dict

            CONVERT s to lowercase
            REMOVE all spaces from s

            FOR each character c in s DO
                IF c is already a key in freq_dict THEN
                    INCREMENT freq_dict[c] by 1
                ELSE
                    SET freq_dict[c] = 1
                END IF
            END FOR

            RETURN freq_dict
        END FUNCTION
    """
    freq_dict = {}
    s = s.lower().replace(" ", "")

    for char in s:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 1
    return freq_dict

print(char_frequency("hello world") )


"""
Let me break down the code for you:

Function Definition:
python
def char_frequency(s):
Defines a function
char_frequency
 that takes a string s as input.
Initialization:
python
freq_dict = {}
s = s.lower().replace(" ", "")
Creates an empty dictionary freq_dict to store character frequencies.
Converts the input string to lowercase and removes all spaces.
Character Counting:
python
for char in s:
    if char in freq_dict:
        freq_dict[char] += 1
    else:
        freq_dict[char] = 1
Iterates through each character in the processed string.
If the character is already a key in the dictionary, it increments the count.
If not, it adds the character to the dictionary with a count of 1.
Return Result:
python
return freq_dict
Returns the dictionary with character frequencies.
Example Usage:
python
print(char_frequency("hello world"))
Calls the function with "hello world" and prints the result.
Example Output: For "hello world", the output is {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}.

This function efficiently counts character frequencies while being case-insensitive and ignoring spaces.
"""