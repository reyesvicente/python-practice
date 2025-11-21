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

"""
# Word Ladder - Line-by-Line Explanation

## Import Statements

```python
from collections import deque
import string
```

**Line 1:** Import `deque` (double-ended queue) from the `collections` module. A deque provides O(1) time complexity for append and pop operations from both ends, making it ideal for BFS queue operations.

**Line 2:** Import the `string` module, which provides `string.ascii_lowercase` containing all lowercase letters 'a' through 'z'.

---

## Function Definition

```python
def word_ladder(start, end, word_list):
```

**Line 3:** Define the function `word_ladder` that takes three parameters:
- `start`: the starting word (string)
- `end`: the target word we want to reach (string)
- `word_list`: list of valid words that can be used in the transformation (list of strings)

---

## Edge Case Check

```python
if end not in word_list:
    return 0
```

**Line 4:** Check if the `end` word exists in `word_list`. If the target word isn't in the list, it's impossible to reach it, so we immediately return 0 (no solution).

**Line 5:** Return 0 to indicate no valid transformation sequence exists.

---

## Data Structure Setup

```python
word_list_set = set(word_list)
word_list_set.add(start)
```

**Line 6:** Convert `word_list` from a list to a set for O(1) lookup time. Checking if a word exists in a set is much faster than checking in a list (O(1) vs O(n)).

**Line 7:** Add the `start` word to the set. This ensures consistency in our algorithm, even though the start word might not originally be in the word list.

---

## BFS Initialization

```python
queue = deque([(start, 1)])
visited = set([start])
```

**Line 8:** Initialize the BFS queue as a deque containing a tuple `(start, 1)`:
- `start`: the current word we're processing
- `1`: the current transformation length (we start at length 1, counting the start word itself)

**Line 9:** Initialize the `visited` set with the `start` word. This prevents us from revisiting the same word, which would create infinite loops and redundant processing.

---

## BFS Main Loop

```python
while queue:
    current_word, length = queue.popleft()
```

**Line 10:** Continue the BFS loop as long as there are words in the queue to process.

**Line 11:** Dequeue the leftmost element from the queue (FIFO - First In, First Out). Unpack the tuple into:
- `current_word`: the word we're currently examining
- `length`: the number of transformations to reach this word from the start

---

## Goal Check

```python
if current_word == end:
    return length
```

**Line 12:** Check if we've reached the target word.

**Line 13:** If we found the end word, return the current `length`. Since BFS explores words level by level (all words at distance 1, then distance 2, etc.), the first time we reach the end word is guaranteed to be the shortest path.

---

## Generate Neighbors (Outer Loop)

```python
for i in range(len(current_word)):
```

**Line 14:** Iterate through each character position in `current_word`. For example, if `current_word` is "hit", we'll process positions 0, 1, and 2 (for 'h', 'i', 't').

---

## Generate Neighbors (Inner Loop)

```python
for c in string.ascii_lowercase:
    new_word = current_word[:i] + c + current_word[i+1:]
```

**Line 15:** For each position `i`, try replacing the character with every letter from 'a' to 'z' (26 possibilities).

**Line 16:** Create a `new_word` by:
- `current_word[:i]`: taking all characters before position `i`
- `c`: inserting the new character at position `i`
- `current_word[i+1:]`: taking all characters after position `i`

**Example:** If `current_word = "hit"`, `i = 0`, and `c = 'b'`, then `new_word = "" + "b" + "it" = "bit"`

---

## Validate and Enqueue Neighbors

```python
if new_word in word_list_set and new_word not in visited:
    visited.add(new_word)
    queue.append((new_word, length + 1))
```

**Line 17:** Check two conditions:
1. `new_word in word_list_set`: The new word must be a valid word from our word list
2. `new_word not in visited`: We haven't processed this word before (avoid cycles)

**Line 18:** Mark `new_word` as visited by adding it to the `visited` set. This prevents us from adding it to the queue again later.

**Line 19:** Add the new word to the queue with an incremented length (`length + 1`). This word will be processed in a future iteration of the while loop.

---

## No Solution Found

```python
return 0
```

**Line 20:** If we exit the while loop without finding the end word, it means no valid transformation sequence exists. Return 0 to indicate failure.

---

## Test Cases

```python
print(word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(word_ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
```

**Line 21:** Test case 1 - Should print `5` because the transformation path exists:
- "hit" → "hot" → "dot" → "dog" → "cog" (5 words total)

**Line 22:** Test case 2 - Should print `0` because "cog" is not in the word list, making transformation impossible.

---

## Algorithm Summary

### Why BFS?
BFS guarantees finding the **shortest path** because it explores all words at distance `k` before exploring words at distance `k+1`. This level-by-level exploration ensures the first time we reach the target is via the shortest route.

### Time Complexity
- **O(M² × N)** where:
  - M = length of each word
  - N = number of words in word_list
  - For each word, we generate M × 26 neighbors, and each neighbor creation takes O(M) time

### Space Complexity
- **O(M × N)** for the queue, visited set, and word_list_set

### Key Optimizations
1. **Set for word_list**: O(1) lookup instead of O(N)
2. **Visited tracking**: Prevents revisiting words and infinite loops
3. **Early termination**: Return immediately when target is found
4. **Deque for queue**: O(1) append and popleft operations
"""