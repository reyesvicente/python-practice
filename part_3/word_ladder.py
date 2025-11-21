# ============================================================================
# PROBLEM 30: Word Ladder Length
# ============================================================================
# Write a function that finds the shortest sequence of words to transform from a start word to an end word.
# Each intermediate word must differ by exactly one letter from the previous word.
# All words must be from the provided word list.
# Example: word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]) should return 5
#          (transformation: "hit" -> "hot" -> "dot" -> "dog" -> "cog")
# Example: word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) should return 0 (no solution)
from collections import deque
import string

def word_ladder(start, end, word_list):
    """
        PSEUDO CODE:
        FUNCTION word_ladder(start, end, word_list):
            // Edge case: if end word is not in word_list, no solution exists
            IF end NOT IN word_list:
                RETURN 0

            // Add start word to word_list for consistency
            word_list_set = SET(word_list)
            word_list_set.ADD(start)

            // Initialize BFS queue with (current_word, transformation_length)
            queue = QUEUE()
            queue.ENQUEUE((start, 1))

            // Track visited words to avoid cycles
            visited = SET()
            visited.ADD(start)

            // BFS traversal
            WHILE queue is NOT empty:
                current_word, length = queue.DEQUEUE()

                // If we reached the end word, return the length
                IF current_word == end:
                    RETURN length

                // Generate all possible one-letter transformations
                FOR each position i in current_word:
                    FOR each letter c in alphabet ('a' to 'z'):
                        // Create a new word by replacing character at position i
                        new_word = current_word[0:i] + c + current_word[i+1:]

                        // Check if this new word is valid and unvisited
                        IF new_word IN word_list_set AND new_word NOT IN visited:
                            visited.ADD(new_word)
                            queue.ENQUEUE((new_word, length + 1))

            // No transformation sequence found
            RETURN 0
    """
    if end not in word_list:
        return 0

    word_list_set = set(word_list)
    word_list_set.add(start)

    queue = deque([(start, 1)])
    visited = set([start])

    while queue:
        current_word, length = queue.popleft()

        if current_word == end:
            return length

        for i in range(len(current_word)):
            for c in string.ascii_lowercase:
                new_word = current_word[:i] + c + current_word[i+1:]

                if new_word in word_list_set and new_word not in visited:
                    visited.add(new_word)
                    queue.append((new_word, length + 1))

    return 0

print(word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))