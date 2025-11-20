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

"""