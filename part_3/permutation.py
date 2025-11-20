# ============================================================================
# PROBLEM 28: Permutations
# ============================================================================
# Write a function that generates all permutations of a list.
# Return a list of tuples, where each tuple is a unique permutation.
# Example: permutations([1, 2, 3]) should return [(1,2,3), (1,3,2), (2,1,3), (2,3,1), (3,1,2), (3,2,1)]
# Hint: You can use recursion or import from itertools

def permutations(lst):
    """
        PSEUDO CODE:
            FUNCTION permutations(lst):
                // Base case: empty list or single element
                IF length of lst <= 1:
                    RETURN [tuple(lst)]

                // Initialize result list
                result = empty list

                // For each element in the list
                FOR i FROM 0 TO length of lst - 1:
                    // Select current element as the "fixed" element
                    current_element = lst[i]

                    // Create remaining list (all elements except current)
                    remaining_elements = lst[0:i] + lst[i+1:end]

                    // Recursively get all permutations of remaining elements
                    sub_permutations = permutations(remaining_elements)

                    // For each sub-permutation, prepend the current element
                    FOR each sub_perm IN sub_permutations:
                        // Combine current element with sub-permutation
                        new_permutation = (current_element) + sub_perm

                        // Add to result
                        ADD new_permutation TO result

                RETURN result
            END FUNCTION
    """
    if len(lst) <= 1:
        return [tuple(lst)]

    result = []
    for i in range(len(lst)):
        current_element = lst[i]
        remaining_elements = lst[:i] + lst[i+1:]
        sub_permutations = permutations(remaining_elements)

        for sub_perm in sub_permutations:
            new_permutation = (current_element,) + sub_perm
            result.append(new_permutation)
    return result

print(permutations([1, 2, 3]))


"""
    - Lines 1–9: File header and problem statement — describes the task (generate all permutations, return list of tuples) and gives a hint.
    - def permutations(lst): — declares the function that accepts one parameter, lst.
    - Triple-quoted block (docstring) — contains pseudocode/documentation only; not executed.
    - if len(lst) <= 1: — base-case check: list has 0 or 1 element.
    - return [tuple(lst)] — return a one-element list containing lst converted to a tuple (e.g., [] -> [()], [x] -> [(x,)]).
    - result = [] — create an empty list to collect permutations.
    - for i in range(len(lst)): — iterate over every index in lst; treat each element as the fixed first item in turn.
    - current_element = lst[i] — pick the element at index i.
    - remaining_elements = lst[:i] + lst[i+1:] — build a new list with all elements except the current one.
    - sub_permutations = permutations(remaining_elements) — recursively compute permutations of the remaining elements.
    - for sub_perm in sub_permutations: — iterate over each returned permutation tuple.
    - new_permutation = (current_element,) + sub_perm — form a new tuple by prepending the current element to the sub-permutation.
    - result.append(new_permutation) — add the new permutation tuple to the results list.
    - return result — after the loops, return the list of all permutation tuples.
    - print(permutations([1, 2, 3])) — call the function with [1,2,3] and print the returned permutations.
    - Final triple-quote lines — stray/empty quotes at the end of the file; harmless but unnecessary and can be removed for cleanliness.
"""